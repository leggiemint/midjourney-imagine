# Legnext API Reference

Complete reference for the Legnext API endpoints used in this skill.

## Authentication

All API requests require authentication via the `x-api-key` header.

```bash
-H "x-api-key: YOUR_API_KEY"
```

**Getting Your API Key:**
1. Visit the Legnext dashboard: https://legnext.ai
2. Navigate to API settings
3. Generate or copy your API key
4. Set it as an environment variable: `export LEGNEXT_API_KEY=your_key_here`

## Base URL

```
https://api.legnext.ai
```

## Endpoints

### 1. Create Image Generation Task

**POST** `/api/v1/diffusion`

Submits a text-to-image generation task.

#### Headers
```
x-api-key: YOUR_API_KEY
Content-Type: application/json
```

#### Request Body
```json
{
  "text": "string (required, 1-8192 characters)",
  "callback": "string (optional, webhook URL)"
}
```

**Parameters:**
- `text` (string, required): The text prompt for image generation. Can include Midjourney parameters (e.g., `--v 7`, `--ar 16:9`)
- `callback` (string, optional): A webhook URL that will receive a POST request when the task completes

#### Response
```json
{
  "job_id": "uuid-string",
  "status": "pending",
  "output": null,
  "meta": {
    "created_at": "timestamp",
    "points_frozen": number,
    "points_consumed": number
  }
}
```

**Response Fields:**
- `job_id`: Unique identifier for tracking the task (UUID format)
- `status`: Initial status will be "pending"
- `output`: Null initially, populated when task completes
- `meta`: Metadata including timestamps and billing information

#### Example Request
```bash
curl -X POST "https://api.legnext.ai/api/v1/diffusion" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "a beautiful sunset over mountains --v 7 --ar 16:9",
    "callback": "https://webhook.site/your-endpoint"
  }'
```

#### Python Example
```python
import requests

url = "https://api.legnext.ai/api/v1/diffusion"
headers = {
    "x-api-key": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "text": "a cyberpunk city at night --v 7 --ar 16:9"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
job_id = result["job_id"]
```

---

### 2. Get Task Status

**GET** `/api/v1/job/{job_id}`

Retrieves the current status and results of a task.

#### Headers
```
x-api-key: YOUR_API_KEY
```

#### URL Parameters
- `job_id` (string, required): The unique identifier of the job (UUID format)

#### Response
```json
{
  "job_id": "uuid-string",
  "status": "completed",
  "output": {
    "images": ["url1", "url2", "url3", "url4"],
    "seed": 123456789
  },
  "meta": {
    "created_at": "timestamp",
    "completed_at": "timestamp",
    "points_frozen": number,
    "points_consumed": number
  },
  "error": null
}
```

**Response Fields:**
- `job_id`: The task identifier
- `status`: One of: `pending`, `staged`, `processing`, `completed`, `failed`
- `output`: Contains result data when status is `completed`
  - `images`: Array of image URLs
  - `seed`: Random seed used for generation
- `meta`: Metadata including timing and billing
- `error`: Error details if status is `failed`

#### Status Values

| Status | Description |
|--------|-------------|
| `pending` | Job is queued and waiting to be processed |
| `staged` | Job is prepared and staged for processing |
| `processing` | Job is currently being processed |
| `completed` | Job has completed successfully |
| `failed` | Job has failed due to an error |

#### Example Request
```bash
curl -X GET "https://api.legnext.ai/api/v1/job/98761286-cdc7-4085-abfe-c9f149ff722b" \
  -H "x-api-key: YOUR_API_KEY"
```

#### Python Example
```python
import requests
import time

url = f"https://api.legnext.ai/api/v1/job/{job_id}"
headers = {"x-api-key": "YOUR_API_KEY"}

# Poll until completed
while True:
    response = requests.get(url, headers=headers)
    result = response.json()

    status = result["status"]
    print(f"Status: {status}")

    if status in ["completed", "failed"]:
        break

    time.sleep(5)  # Wait 5 seconds before next check

if status == "completed":
    images = result["output"]["images"]
    print(f"Generated images: {images}")
```

---

## Workflow

### Complete Image Generation Flow

1. **Submit Task**
   - POST to `/api/v1/diffusion` with your prompt
   - Receive `job_id` in response
   - Initial status will be `pending`

2. **Poll for Completion**
   - GET `/api/v1/job/{job_id}` periodically
   - Check the `status` field
   - Continue polling while status is `pending`, `staged`, or `processing`

3. **Retrieve Results**
   - When status becomes `completed`, extract `output.images`
   - Image URLs are accessible for download
   - Note: Images have a limited storage duration

4. **Handle Errors**
   - If status becomes `failed`, check the `error` field
   - Common errors: invalid prompt, insufficient credits, parameter errors

### Recommended Polling Strategy

- **Interval**: Poll every 5-10 seconds
- **Timeout**: Set a maximum wait time (e.g., 5 minutes)
- **Exponential Backoff**: Optionally increase interval over time

```python
import time

poll_interval = 5  # seconds
max_wait = 300     # 5 minutes
elapsed = 0

while elapsed < max_wait:
    time.sleep(poll_interval)
    elapsed += poll_interval

    # Check status
    # If completed or failed, break
```

---

## Error Handling

### Common HTTP Status Codes

- `200 OK`: Request successful
- `400 Bad Request`: Invalid parameters or prompt
- `401 Unauthorized`: Invalid or missing API key
- `402 Payment Required`: Insufficient credits
- `404 Not Found`: Job ID not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

### Error Response Format
```json
{
  "error": "Error message",
  "details": "Detailed error information"
}
```

### Best Practices

1. **Always validate API key** before making requests
2. **Handle timeouts** - Set reasonable timeouts for HTTP requests
3. **Retry logic** - Implement exponential backoff for transient errors
4. **Validate prompts** - Ensure prompts are within 1-8192 character limit
5. **Store job IDs** - Save job IDs for later retrieval if needed
6. **Monitor credits** - Check meta.points_consumed to track usage

---

## Rate Limits

Rate limits may apply depending on your Legnext plan. Check your dashboard for current limits.

**Typical limits:**
- Requests per minute
- Concurrent jobs
- Total points per day/month

When rate limited, you'll receive a `429` status code. Implement exponential backoff retry logic.

---

## Billing

The Legnext API uses a point-based billing system:

- **points_frozen**: Points reserved when task is submitted
- **points_consumed**: Actual points charged when task completes

Points consumed may vary based on:
- Image complexity
- Parameters used (e.g., `--quality`)
- Generation time
- Model version

Check the `meta` field in responses for billing information.

---

## Image Storage

Generated images are stored temporarily:
- Download and save images you want to keep
- Storage duration varies by plan
- Images may be purged after the retention period

---

## Additional Notes

### Midjourney Parameters
The API supports standard Midjourney parameters in the `text` field:
- Version: `--v 7`, `--v 6`, etc.
- Aspect ratio: `--ar 16:9`, `--ar 1:1`, etc.
- Stylization: `--s 500`, `--s 750`, etc.
- Quality: `--q 1`, `--q 2`, etc.
- And more (see midjourney_parameters.md)

### Callbacks (Webhooks)
If you provide a `callback` URL:
- Legnext will POST to your URL when the task completes
- Payload will include the full task result
- Useful for async workflows without polling

### API Versioning
The current API version is `v1`. Future versions may introduce breaking changes.
Monitor Legnext documentation for updates.

---

## Support

For API issues or questions:
- Documentation: https://docs.legnext.ai
- Dashboard: https://legnext.ai
- Support: Contact via dashboard

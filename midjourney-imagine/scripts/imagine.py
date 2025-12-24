#!/usr/bin/env python3
"""
Submit an image generation task to Legnext API

Usage:
    imagine.py "prompt text here"
    imagine.py "a beautiful sunset --v 7 --ar 16:9"

Environment variables required:
    LEGNEXT_API_KEY: Your Legnext API key from the dashboard
"""

import sys
import os
import json
import requests


def submit_imagine_task(prompt, callback=None):
    """
    Submit an image generation task to Legnext API

    Args:
        prompt (str): The text prompt for image generation (can include Midjourney parameters)
        callback (str, optional): Webhook URL for task completion notifications

    Returns:
        dict: Response containing job_id and status, or error information
    """
    # Get API key from environment
    api_key = os.environ.get('LEGNEXT_API_KEY')
    if not api_key:
        return {
            'error': 'LEGNEXT_API_KEY environment variable not set',
            'details': 'Please set your Legnext API key: export LEGNEXT_API_KEY=your_key_here'
        }

    # Prepare request
    url = 'https://api.legnext.ai/api/v1/diffusion'
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }

    payload = {'text': prompt}
    if callback:
        payload['callback'] = callback

    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            'error': 'API request failed',
            'details': str(e),
            'status_code': getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: imagine.py \"prompt text here\"")
        print("\nExample:")
        print('  imagine.py "a cyberpunk city at night --v 7 --ar 16:9"')
        print("\nMake sure to set LEGNEXT_API_KEY environment variable first:")
        print("  export LEGNEXT_API_KEY=your_key_here")
        sys.exit(1)

    prompt = sys.argv[1]
    callback = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Submitting imagine task...")
    print(f"Prompt: {prompt}")
    if callback:
        print(f"Callback: {callback}")
    print()

    result = submit_imagine_task(prompt, callback)

    # Pretty print result
    print(json.dumps(result, indent=2))

    # Exit with appropriate code
    if 'error' in result:
        sys.exit(1)
    else:
        print(f"\n✓ Task submitted successfully!")
        print(f"Job ID: {result.get('job_id')}")
        print(f"Status: {result.get('status')}")
        sys.exit(0)


if __name__ == '__main__':
    main()

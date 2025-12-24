# Midjourney Prompt Engineering Guide

This guide covers best practices for writing effective Midjourney prompts that produce high-quality images through the Legnext API.

## Basic Principles

### 1. Be Specific and Descriptive
The more detail you provide, the better the results.

**Instead of:**
```
a cat
```

**Try:**
```
a fluffy orange tabby cat sitting on a windowsill, soft morning light, cozy atmosphere
```

### 2. Use Clear, Natural Language
Write as if describing the scene to someone.

**Good:**
```
a modern kitchen with marble countertops, stainless steel appliances, and large windows
```

**Also good:**
```
modern kitchen, marble counters, steel appliances, big windows, bright natural lighting
```

### 3. Order Matters (Usually)
Place the most important elements at the beginning of your prompt.

**Example:**
```
a majestic lion, golden mane, standing on a cliff, sunset background, dramatic lighting
```

## Prompt Structure

### Recommended Format
```
[Subject] [Description] [Environment] [Lighting] [Style] [Parameters]
```

**Example:**
```
a vintage bicycle, rusty frame with flowers in basket, cobblestone street in Paris, golden hour lighting, impressionist painting style --ar 16:9 --v 7
```

## Subject Types

### Photography
Add photography-specific terms:
```
portrait of a woman, professional headshot, studio lighting, 85mm lens, shallow depth of field, bokeh background --v 7
```

### Illustrations
Specify the illustration style:
```
a fantasy dragon, digital illustration, concept art, highly detailed, vibrant colors, trending on artstation --ar 16:9
```

### 3D Renders
Mention rendering techniques:
```
a sleek sports car, 3D render, octane render, studio lighting, metallic paint, reflections, ultra realistic --v 7
```

### Artistic Styles
Reference specific art movements or artists:
```
a cityscape at night, cyberpunk style, neon lights, blade runner aesthetic, cinematic --ar 21:9
```

## Effective Descriptors

### Lighting
- Golden hour, blue hour, sunset, sunrise
- Studio lighting, dramatic lighting, soft lighting
- Backlit, rim lighting, volumetric lighting
- Natural light, harsh shadows, diffused light

### Mood/Atmosphere
- Cozy, dramatic, peaceful, chaotic
- Mysterious, ethereal, gritty, serene
- Dark and moody, bright and cheerful

### Quality/Detail
- Highly detailed, intricate details
- Sharp focus, ultra realistic
- 4K, 8K, high resolution
- Professional, award-winning

### Camera/Perspective
- Wide angle, telephoto, fisheye
- Aerial view, bird's eye view, worm's eye view
- Close-up, macro, extreme close-up
- 35mm, 50mm, 85mm, 200mm lens

### Artistic References
- In the style of [artist name]
- [Art movement] style (impressionism, art deco, etc.)
- Like a [medium] (oil painting, watercolor, pencil sketch)

## Common Patterns

### Pattern 1: Product Photography
```
[Product], product photography, white background, studio lighting, commercial, high resolution --ar 1:1 --v 7
```

### Pattern 2: Character Design
```
[Character description], character design, full body, concept art, detailed costume, white background --ar 3:4 --v 7
```

### Pattern 3: Landscape Scene
```
[Location], landscape photography, [time of day], [weather], dramatic sky, wide angle --ar 16:9 --v 7
```

### Pattern 4: Interior Design
```
[Room type], interior design, [style], natural lighting, cozy atmosphere, architectural photography --ar 16:9 --v 7
```

## Advanced Techniques

### Multi-Prompting with ::
Use `::` to separate concepts and assign weights:

```
cat::2 dog::1
```
This gives twice as much weight to "cat" compared to "dog".

### Using Negative Prompts
Exclude unwanted elements with `--no`:

```
a clean modern office --no clutter --no people --no windows
```

### Consistency with Seeds
Reuse seed values for similar variations:

```
a magical forest --seed 12345 --v 7
```

## What to Avoid

### 1. Overly Long Prompts
Midjourney has a character limit. Be concise.

**Too long:**
```
a beautiful amazing stunning gorgeous incredible fantastic wonderful excellent perfect majestic cat
```

**Better:**
```
a majestic cat, regal pose, dramatic lighting
```

### 2. Contradictory Terms
Avoid conflicting descriptions:

**Confusing:**
```
a dark bright scene
```

**Better:**
```
a dimly lit scene with bright highlights
```

### 3. Abstract Concepts Without Visual Cues
Give visual context to abstract ideas:

**Vague:**
```
happiness
```

**Better:**
```
a joyful family laughing together at a picnic, sunny day, bright colors, warm atmosphere
```

## Style References

### Photographic Styles
- Documentary photography
- Fashion photography
- Street photography
- Architectural photography
- Wildlife photography
- Astrophotography

### Art Styles
- Photorealistic
- Impressionist
- Surrealist
- Abstract
- Minimalist
- Pop art
- Art nouveau
- Cyberpunk
- Steampunk

### Media Types
- Oil painting
- Watercolor
- Digital art
- Pencil sketch
- Ink drawing
- 3D render
- Clay sculpture
- Vector art

## Testing and Iteration

1. **Start Simple**: Begin with a basic prompt
2. **Add Details Gradually**: Refine one aspect at a time
3. **Use Variations**: Try different phrasings for the same concept
4. **Experiment with Parameters**: Test different `--s`, `--chaos`, `--ar` values
5. **Save Good Seeds**: Note seed values from successful generations

## Examples by Use Case

### Logo Design
```
minimalist logo design for a coffee shop, simple line art, modern, clean, vector style --v 7
```

### Book Cover
```
fantasy book cover, mysterious forest with glowing portal, magical atmosphere, professional book cover design --ar 3:4 --v 7
```

### Social Media Post
```
motivational quote background, gradient colors, abstract shapes, modern design, instagram post --ar 4:5 --v 7
```

### Website Hero Image
```
tech startup hero image, modern office space, diverse team collaborating, bright and professional, wide angle --ar 21:9 --v 7
```

### Product Mockup
```
smartphone mockup, hand holding phone, clean background, lifestyle photography, natural lighting --ar 9:16 --v 7
```

## Resources

- Experiment with different parameter combinations
- Study successful prompts from the Midjourney community
- Keep a prompt library of patterns that work well for your needs
- Use reference images when possible (image URLs in prompts)

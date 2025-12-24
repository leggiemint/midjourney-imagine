# Midjourney Parameters Reference

This document provides a comprehensive reference for Midjourney parameters that can be included in prompts submitted to the Legnext API.

## Version Parameters

### --v (Version)
Controls which Midjourney model version to use.

**Common versions:**
- `--v 7` - Latest version (v7, draft mode)
- `--v 6` - Version 6
- `--v 5.2` - Version 5.2
- `--v 5.1` - Version 5.1
- `--v 5` - Version 5

**Example:**
```
a beautiful landscape --v 7
```

### --draft
Use draft mode for faster generation (available with v7).

**Example:**
```
a cyberpunk city --v 7 --draft
```

## Aspect Ratio

### --ar (Aspect Ratio)
Sets the width-to-height ratio of the generated image.

**Common ratios:**
- `--ar 1:1` - Square (default)
- `--ar 16:9` - Widescreen landscape
- `--ar 9:16` - Portrait (mobile)
- `--ar 4:3` - Traditional photo
- `--ar 3:2` - Standard photo
- `--ar 21:9` - Ultra-wide
- `--ar 7:4` - Close to 16:9

**Example:**
```
a mountain vista --ar 16:9
```

## Style Parameters

### --stylize or --s
Controls how much Midjourney applies its artistic interpretation.

**Values:** 0-1000
- Lower values (0-100): More literal interpretation, closer to prompt
- Default: Varies by version
- Higher values (500-1000): More artistic, Midjourney's aesthetic

**Example:**
```
a portrait of a cat --s 750
```

### --style
Applies specific style variations (version-dependent).

**Common styles:**
- `--style raw` - More photographic, less stylized
- `--style scenic` - Landscape-optimized (v7)

**Example:**
```
a photograph of a city street --style raw
```

## Quality and Speed

### --quality or --q
Controls rendering quality and generation time.

**Values:**
- `.25` - Fastest, lowest quality (4x faster, 1/4 cost)
- `.5` - Half quality (2x faster, 1/2 cost)
- `1` - Standard quality (default)
- `2` - Highest quality (2x slower, 2x cost, not always available)

**Example:**
```
a detailed illustration --q 2
```

### --fast / --relax / --turbo
Controls generation speed priority (requires specific plan).

**Example:**
```
a quick sketch --fast
```

## Creativity Parameters

### --chaos or --c
Controls variation in results.

**Values:** 0-100
- 0: More predictable, consistent results
- 100: More varied, unexpected results

**Example:**
```
abstract art --chaos 80
```

### --weird or --w
Introduces unconventional aesthetics (v7+).

**Values:** 0-3000
- 0: Normal
- Higher values: More unusual/experimental

**Example:**
```
a surreal landscape --weird 1500
```

## Seed

### --seed
Sets a random seed for reproducibility.

**Values:** 0-4294967295
- Use the same seed with the same prompt for similar results
- Different seeds produce different variations

**Example:**
```
a fantasy castle --seed 12345
```

## Negative Prompting

### --no
Excludes specific elements from the generation.

**Example:**
```
a beach scene --no people --no clouds
```

## Image Weight

### --iw (Image Weight)
Controls the influence of an image prompt (when using image URLs).

**Values:** 0-2
- Default: 1
- Higher values: Image has more influence

**Example:**
```
https://example.com/image.jpg a painting --iw 1.5
```

## Other Parameters

### --tile
Generates seamless tiling patterns.

**Example:**
```
floral pattern --tile
```

### --video
Creates a video of the generation process (may not be available in all versions).

## Parameter Combinations

Parameters can be combined in any order:

```
a majestic lion in savanna --v 7 --ar 16:9 --s 500 --q 1 --chaos 20
```

## Notes

- Parameters are space-separated and start with `--`
- Parameter order doesn't matter
- Not all parameters work with all versions
- Some parameters may affect generation cost
- Check Legnext documentation for version-specific parameter support

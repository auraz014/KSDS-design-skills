---
name: webm-to-webp
description: Convert animated WebM files to WebP, optimizing size while preserving visual quality, timing, dimensions, and source transparency, with a specified loop count. Use when the user asks to convert, compress, optimize, or prepare WebM motion assets for the web as WebP, especially VP9 WebM files with alpha transparency.
---

# WebM to WebP

Use `scripts/convert_webm_to_webp.sh` for the standard conversion. Preserve the
source WebM. User instructions take precedence over defaults below; do not treat
the helper's options as the limit of the whole task.

## Required input

Require both:

1. A concrete WebM file path or attached WebM file.
2. A loop count from 0 to 65535.

Resolve file references from attachments, known paths, and relevant context
before asking. Accept loop instructions already given for this task, including
natural language such as “无限循环” or “播放一次”; do not ask for the numeric form.
If a required value genuinely remains unknown, ask only for that value. Source
inspection can proceed while waiting for the loop choice. Explain only when useful:

- `0` means infinite looping.
- `1` means one complete play.
- `N >= 2` means N complete plays.

Apply a batch-wide loop instruction to all named files without reconfirming.
Ask only if its scope genuinely remains ambiguous. Do not invent a default loop
count or reuse an unrelated task's choice.

## Dependencies

Require `ffmpeg`, `ffprobe`, and `webpmux`. Use ImageMagick's `magick` only for
optional visual comparison. If a dependency is missing, check available local
equivalents first. Install only within existing user authorization and platform
permissions; otherwise report the specific dependency and request the missing
authorization once. A missing optional comparison tool does not block conversion.

## Workflow

1. Inspect the source with `ffprobe`. Pay attention to codec, dimensions,
   duration, frame rate, and the `alpha_mode` tag.
2. Use the requested destination. If it exists and replacement is already
   authorized, proceed without asking again. Otherwise choose an unused filename
   when the user has not required an exact path; ask only when satisfying an exact
   destination requires new overwrite authorization. Never delete the source WebM.
3. Choose a WebP preset:
   - Use `text` for titles or typography-heavy motion.
   - Use `icon` for small icons.
   - Use `drawing` for logos and flat UI illustration.
   - Use `default` when the content is unknown.
4. Start with one Q85 output in a temporary directory, or the user's specified
   quality. Add candidates only to address observed defects or a size requirement:
   - Try Q92 for quality defects, or Q80 for additional compression.
   - Keep resolution and frame timing unchanged.
   - Do not reduce frame rate or dimensions unless the user authorizes it.
5. Inspect representative frames and motion when available; for transparent
   assets, check edges against light and dark backgrounds. If comparing candidates,
   select the smallest acceptable one. When visual inspection is unavailable,
   retain Q85 unless instructed otherwise, report that limitation, and do not
   generate extra candidates that cannot be meaningfully compared. Do not go below
   Q80 unless the user explicitly prioritizes file size.
6. Write only the selected candidate to the destination.
7. Validate canvas size, total duration, transparency, loop count, and output
   size. An animation encoder may merge visually identical adjacent frames; do
   not require the output frame count to equal the source when total duration and
   playback are preserved.
8. Return a clickable output path plus before/after sizes and the verified loop
   behavior. State any unmet requirement or unverified visual quality; successful
   encoding alone does not establish quality equivalence or size reduction.

## Script usage

```bash
scripts/convert_webm_to_webp.sh INPUT.webm \
  --loop 1 \
  --output OUTPUT.webp \
  --quality 85 \
  --preset drawing
```

Add `--overwrite` when replacement of that destination is authorized; existing
authorization suffices.

The script forces `libvpx-vp9` for VP9 input so an alpha channel is decoded
instead of appearing as black. It writes through a temporary file and rejects
an output that loses dimensions, timing, loop metadata, or declared alpha.

## Quality rules

- Optimize encoding quality before changing resolution or frame rate.
- Treat transparent edges as a critical quality feature.
- Keep the alpha channel when the WebM declares VP9 alpha.
- Use lossless WebP when requested or when lossy candidates cannot meet the quality
  requirement. The helper supports lossy encoding only: use an appropriate encoder
  invocation for lossless output and retain the same output checks, rather than
  passing an unsupported option. Lossless animation can be much larger than WebM.
- WebP is not guaranteed to be smaller than WebM. Report actual sizes. For a hard
  size limit, try suitable in-scope encoding adjustments; if meeting it requires
  unauthorized changes to dimensions or frame rate, present the concrete tradeoff
  instead of silently degrading the asset or claiming completion.
- Set the loop count in the WebP container; ordinary HTML `<img>` elements do
  not provide a reliable API for overriding it.

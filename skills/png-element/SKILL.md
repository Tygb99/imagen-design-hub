---
name: png-element
description: Recommend and create DesignHub native transparent PNG elements with image_gen, alpha-preserving finishing, QA, and metadata.
---

# PNG Element

[Korean](SKILL.ko.md)

Read [shared rules](../../SKILL.md). Recommendations contain 3–5 concrete concepts with subject, style, use case and buyer-facing keywords.

1. Follow the installed imagegen skill; use built-in image_gen and explicitly request a genuinely transparent background, one asset per call.
2. Preserve returned originals under assets/source-imagegen/. Do not require a fresh child session, browser, API key, chroma key or background-removal pass.
3. Verify fully transparent exterior pixels and a nonempty subject; preserve intentional partial alpha. A painted checkerboard is a failed generation: regenerate with a focused correction instead of automatically keying it.
4. Finish a separate copy with Pillow or the project processor for trim, size, DPI and file size. Photopea is optional for necessary manual edits or explicit requests.
5. Inspect checkerboard, white and dark composites for internal holes, faint fringe and clipping. Never globally remove purple/green or low-alpha pixels.
6. Prepare unique filenames and PNG element CSV with 20–25 buyer-facing keywords. Use [upload-csv](../upload-csv/SKILL.md) for authorized upload.

Preserve smooth partial alpha for glass and translucent effects. Do not run GIF chroma cleanup here. If native output repeatedly fails, report the failure and choose a fallback only within the requested scope.

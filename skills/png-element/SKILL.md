---
name: png-element
description: Recommend and create DesignHub native transparent PNG elements with image_gen, alpha-preserving finishing, QA, and metadata.
---

# PNG Element

[Korean](SKILL.ko.md)

Read [shared rules](../../SKILL.md). Recommendations contain 3–5 concrete concepts with subject, style, use case and buyer-facing keywords.

Follow the Images 2.6 baseline in the shared rules while using only options exposed by the actual native tool. For reference edits or a matching series, inspect the target first, reuse the accepted reference through supported image inputs, and name the change while preserving identity, geometry, palette and partial alpha. Preserve every source/revision separately. API quality, complexity and markup controls are optional only on an explicitly selected API path; see [controls](../../references/2026-11-06-22-36-21-images-2-6.md).

1. Check native image-tool availability using the shared rules, then follow the installed imagegen skill and request a genuinely transparent background, one asset per call. If no native tool is exposed, stop and follow [image-generation diagnostics](../../references/image-generation-troubleshooting.md); do not jump straight to an API-key fallback or assume the account is Free.
2. Preserve returned originals under assets/source-imagegen/. Do not require a fresh child session, browser, API key, chroma key or background-removal pass.
3. Finish a separate copy with Pillow or the project processor for size, DPI and file size. Trim with `python3 scripts/designhub_preflight.py crop <in.png> <out.png>` from this plugin's root; it keeps DPI.
4. Prepare unique filenames and PNG element CSV with 20–25 buyer-facing keywords. Use [upload-csv](../upload-csv/SKILL.md) for authorized upload.
5. Immediately before upload, run `python3 scripts/designhub_preflight.py margin <final.png> ...`. Upload only files that print PASS: margin (0,0,0,0) on every side and a short side of at least 700 px. FAIL exits non-zero; do not upload that file. Six PNG elements were rejected on 2026-10-11 for leftover margins even though this route already said trim ([records](../../records/designhub-rejected-elements.csv)).

Both commands treat alpha at or below 8 of 255 (about 3%) as empty canvas. Faint shadow or glow pixels that weak are invisible on a page but widen a plain `getbbox()` trim and leave a visible margin. Keep this threshold for crop and margin alike; change it only with the user's approval.

Preserve smooth partial alpha for glass and translucent effects. Do not run GIF chroma cleanup here. If native output repeatedly fails, report the failure and choose a fallback only within the requested scope.

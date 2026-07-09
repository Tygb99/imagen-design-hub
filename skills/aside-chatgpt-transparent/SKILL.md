---
name: aside-chatgpt-transparent
description: Use for MiriCanvas or DesignHub transparent PNG batches generated through Aside controlling ChatGPT native transparent image output: one-image-at-a-time prompting, 2-minute generation waits, download capture, local alpha/background QA, Photopea finishing, 350 DPI resizing, metadata CSV rows, and buyer-facing keyword cleanup. Use this whenever the user mentions Aside, ChatGPT, GPT Images native transparent, direct transparent PNG generation, local QA, Photopea post-processing, or keyword creation for DesignHub PNG elements.
metadata:
  short-description: Aside + ChatGPT native transparent PNG route with QA, Photopea, and keywords
---

# Imagen Design Hub: Aside ChatGPT Transparent

[Korean version](SKILL.ko.md)

Use this route when the user wants ChatGPT/Aside to create native transparent PNG elements, then expects local validation, Photopea finishing, and DesignHub-ready metadata. This is different from the chroma-key `png-element` route: here the source is already RGBA/native transparent, so the risk moves from key-color removal to alpha quality, hidden transparent holes, low resolution, and incomplete subjects.

## Read First

1. Read the installed `aside-browser` skill when you need to drive ChatGPT through Aside.
2. Read `../../skills/png-element/SKILL.md` for the shared PNG output contract.
3. Read `../../references/keyword-generation.md` before writing keywords.
4. Read `../../SKILL.md` when the task crosses into upload CSV, SVG/GIF, JPG backgrounds, or shared route selection.

## When To Use

Use this route for:

- User asks for `aside`, `ChatGPT`, `native transparent`, GPT Images transparent PNG, or direct transparent output.
- Chroma-key removal is undesirable because the subject has complex edges, glass, hair, fabric, flags, holes, or colors that would conflict with practical key colors.
- The batch still needs DesignHub/MiriCanvas PNG element finishing: larger than the native 1024 px output, 350 DPI, tight crop, and CSV metadata.
- The user asks for local inspection after download before upload.

Do not use this route for JPG backgrounds, SVG, GIF, or post-upload CSV roundtrips. Route those to the matching plugin skill.

## Hard Boundaries

- Do not upload, submit, or change DesignHub state unless the user explicitly asks for that external action.
- Do not treat ChatGPT native transparency as automatically clean. It can hide transparent pixels inside white areas, between symbols, or under anti-aliased details.
- Do not overwrite original downloads. Preserve them first, then create processed outputs.
- Do not crop final upload PNGs out of contact sheets.
- If ChatGPT repeatedly says it cannot create the image or stays stuck beyond the agreed wait window, record the outage/stall and stop or ask before continuing.

## Suggested Folder Layout

```text
outputs/<run-id>/
  assets/source-aside-chatgpt/
  assets/processed-aside-chatgpt/
  assets/replaced-or-repaired/<timestamp>/
  metadata/aside-chatgpt-preupload.csv
  review/aside-chatgpt/
  logs/aside-chatgpt-generation.json
```

If the current project already uses a different established folder shape, match it and explain the mapping in the final report.

## Aside Generation Workflow

1. Confirm the batch topic, count, and any factual visual rules before opening ChatGPT.
2. Use `aside exec` for logged-in ChatGPT generation. Use `aside repl` when you need deterministic screenshots, snapshots, or download evidence.
3. Generate one image at a time unless the user explicitly asks for comparison candidates.
4. After each prompt, wait up to about 2 minutes for completion when the user gives that rule. If no image appears, record the exact visible state.
5. Download the image into Aside session artifacts first, then copy it into `assets/source-aside-chatgpt/`.
6. Verify every download locally before moving to the next image:
   - file exists and byte size is nonzero
   - PNG signature is valid
   - mode is RGBA or has an alpha channel
   - transparent pixels exist
   - image is not a UI screenshot, error panel, checkerboard, watermark, or duplicated failed candidate
7. Keep a manifest with prompt, source path, size, alpha extrema, hash, and any user-visible ChatGPT status.

## Prompt Shape

Use concise prompts with explicit negative constraints:

```text
Create one native transparent PNG element for MiriCanvas/DesignHub.
Subject: <single subject>
Style: <style>
Composition: fully visible subject, centered, no cropping, no extra background scene
Transparency: native transparent background, no checkerboard, no solid background, no drop shadow unless requested
Quality constraints: no text, no watermark, no logo, no UI frame, no signature
Factual constraints: <flags, symbols, counts, positions, required references>
```

For factual symbols such as national flags, badges, numbers, or historical objects, verify the visual rules from a reliable source before accepting the image. If the user provides a strict local criterion file, use that as the source of truth.

## Local QA

Create review sheets for checkerboard, white, and dark backgrounds. Inspect at full view and zoomed detail.

Check:

- Subject is fully visible and not clipped.
- Alpha bbox is tight enough for the current project rule.
- No rectangular background residue remains.
- White or pale subject areas do not contain hidden transparent holes that only show on dark backgrounds.
- Fine details are not accidentally transparent or semi-transparent.
- Important factual details are correct and countable.
- Multiple downloads are not duplicates unless the user intentionally accepted duplicates.

For hidden transparency checks, scan for transparent or very-low-alpha components that are not connected to the image border. Flag any large interior component for manual review. For white flags, paper, clothing, and signs, inspect dark background previews especially carefully.

## Photopea Finishing

ChatGPT native transparent output is often 1024 px and low DPI. Treat it as source, not final.

1. Preserve source downloads in `assets/source-aside-chatgpt/`.
2. Run the project Photopea runner when one exists. For `miricanvas-design`, prefer:
   ```bash
   node src/cli.mjs photopea-runner --run outputs/<run-id>
   ```
3. If no project runner exists, create or use the bundled runner pattern with `../../scripts/write_photopea_runner.py`.
4. Final PNGs should satisfy the local DesignHub convention unless the user says otherwise:
   - PNG with alpha
   - at least 2500 px on the short side
   - 350 DPI
   - tight crop, usually margin 0 to under 3 px
5. Validate again after Photopea because resize/trim can expose low-alpha holes or edge artifacts.

## Metadata And Keywords

Create CSV rows only after the processed filenames are settled.

Default headers:

```text
fileName,uniqueId,elementName,keywords,tier,contentType
```

Rules:

- `fileName`: basename matching the processed PNG, usually without extension when the local CSV contract expects it.
- `uniqueId`: blank before DesignHub file upload.
- `tier`: `Premium` unless the user says otherwise.
- `contentType`: `PNG element`.
- `keywords`: 20 to 25 unique buyer-facing keywords.
- Remove process/file/admin terms such as `ChatGPT`, `Aside`, `Photopea`, `imagegen`, `native transparent`, `PNG`, `DPI`, `CSV`, `DesignHub`, `MiriCanvas`, `Premium`, dates, run IDs, and upload labels.
- Preserve user-required event/topic terms such as `3.1절`, `광복절`, or a current challenge topic when they are semantically relevant.

## Repair Or Replace Decisions

- If the subject is structurally wrong, badly clipped, or factually incorrect, replace the image rather than repairing it.
- If the only issue is a localized alpha defect inside an otherwise good image, preserve the original and repair a copy. Keep a repair manifest with before/after hashes and review sheets.
- If factual criteria are strict, prefer a clear replacement over heavy local painting that changes the generated subject.

## Final Report

Report:

- Aside/ChatGPT surface used and whether generation was one-at-a-time.
- Source folder and processed folder.
- Metadata CSV path and keyword count.
- Review sheets for checkerboard, white, and dark backgrounds.
- Photopea use and final PNG specs.
- Any replacements, repairs, or rejected downloads.
- Whether external upload/CSV upload/final submission happened. If not, say it did not happen.

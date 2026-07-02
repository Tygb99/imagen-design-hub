---
name: png-element
description: Use for MiriCanvas or DesignHub PNG element work: imagegen source art, chroma-key background removal, transparent PNG cutouts, Photopea finishing, upload-safe PNG basenames, and PNG element CSV rows.
metadata:
  short-description: DesignHub PNG element route with image-gen, chroma cleanup, Photopea, and fringe QA
---

# Imagen Design Hub: PNG Element

[Korean version](SKILL.ko.md)

Use this route when the user says `png요소`, transparent PNG, cutout, sticker, element, background removal, Photopea, upload-ready alpha asset, or magenta/purple fringe cleanup.

This skill is intentionally compact. The full PNG-element workflow lives in `references/full-workflow.md`; the Korean companion is `references/full-workflow.ko.md`. Read only the sections needed for the current phase, then execute them exactly.

Shared route map: read `../../SKILL.md` if you need the full DesignHub plugin routing across PNG, JPG, SVG, GIF, and upload CSV.

## Required First Steps

1. Open `references/full-workflow.md`.
2. Read through **Route Triggers**, **Core Rules**, **Chroma-Key Workflow**, **Magenta Fringe Decontamination**, **Output Contract**, and **Validation** before generating sources, removing backgrounds, or calling a PNG batch ready.
3. If the task touches plugin-wide routing, CSV upload, SVG/GIF routes, or shared metadata rules, also read `../../SKILL.md`.

## Non-Negotiables

- Use the installed `$image-gen` skill for source creation so generation runs in a fresh `codex exec` session. The underlying image tool is built-in `image_gen`.
- Preserve source files in `assets/source-imagegen/`; never overwrite original generation outputs.
- Generate on a perfectly flat solid chroma-key background. Do not ask imagegen for transparent or checkerboard backgrounds.
- For multiple standalone PNG elements, generate one source image per element. Do not generate a crowded sheet and crop it into separate assets later.
- Run `../../scripts/chroma_key.py` first into `assets/raw/`; do not use `.system/imagegen/remove_chroma_key.py` for DesignHub PNG-element runs.
- Do not use `../../scripts/remove_chroma_key.py` unless the user explicitly asks for a comparison or fallback.
- Use magenta-fringe decontamination only when the key is magenta/purple and the prompt forbade pink, purple, and magenta inside the subject.
- For wind, breeze, air, mist, or other translucent effects, an intentional light/neutral outline or stroke is a good preservation choice when it keeps the effect readable and prevents key-color bleed.
- For upload-ready DesignHub PNGs, finish through Photopea or the project Photopea runner into `assets/processed/`.
- Treat contact sheets as preview artifacts only. Never crop final upload PNGs out of a contact sheet.
- External DesignHub upload/submission is off-limits unless the user explicitly confirms it.

## Folder Structure

This skill follows the compact `ulw-loop`-style layout:

- `SKILL.md`: compact entrypoint, trigger, first steps, and non-negotiables
- `SKILL.ko.md`: Korean companion entrypoint
- `references/full-workflow.md`: full English workflow
- `references/full-workflow.ko.md`: full Korean workflow
- `agents/openai.yaml`: app/plugin-facing prompt metadata

## Codex Tool Mapping

| Workflow intent | Codex surface |
| --- | --- |
| Source generation | `$image-gen` skill, backed by built-in `image_gen` |
| Alpha extraction | `../../scripts/chroma_key.py` |
| Upload-ready PNG finishing | Photopea or project Photopea runner |
| Visual QA | checkerboard, white, and dark previews |
| Metadata | DesignHub CSV with `contentType` value `PNG element` |

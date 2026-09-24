---
name: imagen-design-hub
description: Recommend and prepare DesignHub native transparent PNG elements, JPG backgrounds, SVG elements, sprite-gen GIF animations, and upload CSV metadata.
---

# Imagen Design Hub 0.5.1

[Korean](SKILL.ko.md)

Start with PNG element recommendations when the user asks what to create: suggest 3–5 concrete concepts with subject, style, use case, and buyer-facing keywords.

## Routes

- Transparent PNG: [png-element](skills/png-element/SKILL.md). Use Codex built-in image_gen with a genuinely transparent background; preserve and inspect native alpha.
- JPG background: [jpg-background](skills/jpg-background/SKILL.md). Full-bleed backgrounds, source PNG preserved, final RGB JPG and `Background` CSV.
- SVG: [svg-beta](skills/svg-beta/SKILL.md). True vectors, not embedded raster images.
- GIF: [gif](skills/gif/SKILL.md). Use the installed sprite-gen component-row pipeline, then inspect actual playback and transparency.
- Upload and metadata: [upload-csv](skills/upload-csv/SKILL.md). Computer Use for live DesignHub actions; local tools for CSV merging.

## Native transparency

[OpenAI's Images 2.5 announcement](https://openai.com/index/introducing-chatgpt-images-2-5/) confirms Codex availability and transparent-background support. Request native transparency first. Tool availability does not identify the exact backend variant; never claim Flare or Sunburst without returned evidence.

Generate one source per standalone PNG element. Preserve source files under `assets/source-imagegen/`; write derived files separately. An RGBA label alone is not proof: require fully transparent background pixels and inspect checkerboard, white, and dark composites. Preserve intentional partial alpha, especially glass, mist, hair, and glow. Never globally neutralize purple/green pixels or flatten alpha to make a check pass.

The old mandatory chroma-key removal, blanket fringe-decontamination recipes, and dedicated Aside/ChatGPT transparency route are retired. Browser generation is optional only when explicitly requested; native PNG creation does not require Aside, another login, or an API key.

PNG finishing uses Pillow or an existing project processor for trim, size and DPI. Photopea is optional for edits those tools cannot reproduce or when explicitly requested. Bundled Photopea and unique-name helpers remain available.

Sprite-gen's animation row pipeline still uses its own chroma extraction. This is a GIF-specific dependency, not a reason to key native PNGs. Read the installed sprite-gen version and its docs; do not copy its engine into this plugin.

## Output and metadata

Respect project-specific constraints. The local DesignHub PNG convention is at least 2500 px on each side, at most 9000 px, 350 DPI, under 50 MB, with tight alpha bounds and no subject clipping. GIF candidates are 700–1920 px per side and under 25 MB; validate current official rules before submission.

Use the exact CSV header:
`fileName,uniqueId,elementName,keywords,tier,contentType`.

Use 20–25 unique buyer-facing keywords and read [keyword guidance](references/keyword-generation.md). Describe subject, form, style, use, season, audience and color. Omit tool names, production steps, file formats, run IDs, dates, and administrative terms. Do not mix languages unless requested.

Use `PNG element`, `GIF`, `SVG element`, `Background`, `Photo`, or `Photo(Cut-out)` as appropriate; default tier is `Premium`. Keep preupload uniqueId blank. After upload, download DesignHub's CSV, preserve its rows and IDs, merge metadata, reupload, and verify the processed-row count. Match basenames to actual files and the downloaded CSV. The bundled `scripts/prepare_designhub_unique_upload.py` prepares separate unique-name copies.

Existing user authorization remains valid; do not ask twice for the same files and destination. Report file upload, metadata registration, and review status separately. Do not change unrelated selected items.

## Verification and handoff

Check image signature, dimensions, DPI, alpha distribution, full subject bounds, file size, and matching CSV rows. Inspect all PNGs and GIF frames on checkerboard, white and dark backgrounds; GIF motion must be reviewed in playback. Preserve sources and failed candidates. Report actual paths, source/tool provenance, measured checks, quality limitations, and whether external actions occurred.

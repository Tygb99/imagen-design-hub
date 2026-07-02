---
name: png-element-full-workflow
description: Full workflow for MiriCanvas and DesignHub PNG element generation, chroma-key cleanup, Photopea finishing, magenta-fringe QA, and CSV validation.
---

# PNG Element Full Workflow

Use this workflow for transparent stickers, illustrations, objects, cutouts, PNG elements, background removal, Photopea finishing, or upload-ready alpha assets for MiriCanvas / DesignHub.

## Route Triggers

Use the `png-element` route when the user mentions any of:

- `png요소`, PNG element, sticker, cutout, transparent PNG, alpha asset
- background removal, chroma key, Photopea, upload-ready PNG
- magenta/purple fringe cleanup after key removal

Read `../../SKILL.md` when the request crosses into JPG backgrounds, SVG/GIF routes, DesignHub CSV upload, or plugin-wide routing.

## Core Rules

- Use the installed `$image-gen` skill for source creation so generation runs in a fresh `codex exec` session. The underlying image tool is built-in `image_gen`.
- Generate on a perfectly flat solid chroma-key background.
- Do not request transparent or checkerboard backgrounds from imagegen.
- Pick a key color that does not overlap with the subject. Default to `#8000ff` only when the subject does not use similar purple. For green subjects use magenta; for blue subjects avoid blue.
- Tell imagegen not to use the key color anywhere inside the subject.
- If the key is magenta or purple and the subject intentionally avoids pink, purple, and magenta, run magenta-fringe decontamination after alpha extraction.
- If the subject has real pink, purple, or magenta details, do not run magenta-fringe decontamination. Choose a safer key color or mask the subject details instead.
- For semi-transparent effects such as wind, breeze, air flow, mist, glass, water spray, or motion lines, background color tests are not enough. If the effect absorbs the key color, regenerate with a safer key or add an intentional light/neutral outline or stroke around the effect before key removal.
- For multiple standalone PNG elements, generate one source image per element. Do not generate a crowded sheet and crop it into separate assets later; separated enlargements can reveal stair-stepped edges and weak anti-aliasing.
- Preserve source files in `assets/source-imagegen/`.
- Run `../../scripts/chroma_key.py` first into `assets/raw/`.
- Do not use `.system/imagegen/remove_chroma_key.py` for DesignHub PNG-element runs.
- Do not use `../../scripts/remove_chroma_key.py` unless the user explicitly asks for a comparison or fallback.
- For upload-ready DesignHub PNGs, finish through Photopea or the project Photopea runner into `assets/processed/`.
- Treat review contact sheets as preview artifacts only. Never crop final upload PNGs out of a contact sheet.

## Chroma-Key Workflow

Run commands from `skills/png-element/`, or adjust paths if running from the plugin root.

Run with edge-connected cleanup:

```bash
python ../../scripts/chroma_key.py \
  --input "<source.png>" \
  --output "<raw-alpha.png>" \
  --background "<KEY_COLOR>" \
  --tolerance 48 \
  --scope edge \
  --dpi 350
```

If subject details close to the key color disappear, regenerate with a safer background color instead of widening tolerance.

Prefer edge-connected removal over broad global tolerance. Broad tolerance can erase interior subject details when the fan, object, or pattern contains colors close to the key color. If interior details are damaged, lower enclosed removal or regenerate on a safer key color before accepting the result.

After chroma-key removal and Photopea finishing, inspect edges at magnified scale on checkerboard, white, and dark backgrounds. If outlines still look stair-stepped or jagged, rerun finishing from the original per-element source or regenerate the element individually; do not accept a locally enlarged crop as upload-ready.

## Magenta Fringe Decontamination

Use this only for magenta or purple key-color runs where the prompt forbade pink, purple, and magenta inside the subject. This fixes key-color contamination on anti-aliased edges; it is not a general color correction step.

After alpha extraction and before final Photopea/contact-sheet approval, scan visible pixels where alpha is greater than zero. Any pixel with `red > green` and `blue > green` is treated as magenta cast. Replace that pixel's RGB with `(green, green, green)` and keep alpha unchanged.

Verify the count before and after. Accept the result only when the remaining visible magenta-cast pixel count is `0`, transparent-pixel RGB remains clean, and dark preview (`#282828`) shows no purple outline. Also inspect white and checkerboard previews.

For non-magenta keys, prefer a safer key color or regeneration. Do not silently apply channel-neutralization to real subject colors.

## Output Contract

- Final upload candidates are PNG files with alpha.
- Use tight alpha bbox unless the project says otherwise.
- For the current MiriCanvas DesignHub submission flow, keep final PNGs at 350 DPI and at least 2500 px on each side.
- CSV rows use `contentType` value `PNG element`.
- Keywords must be 20 to 25 unique buyer-facing terms.
- Generate keywords with the plugin-wide guide at `../../../references/keyword-generation.md`; prioritize subject/object, element form, style, use case, season/event, audience/industry, and color/mood.
- Before DesignHub upload, prepare unique upload-safe basenames with `../../scripts/prepare_designhub_unique_upload.py` when reupload collisions are possible.

## Validation

Check all of these before calling the batch ready:

- alpha channel exists
- transparent corners pass
- no visible key-color fringe on checkerboard, white, and dark previews
- magenta-key runs have `0` remaining visible magenta-cast pixels after decontamination, unless real subject magenta/purple detail required a different key or manual mask
- no subject interior detail was erased because it matched the key color
- translucent wind, breeze, air, mist, or motion effects remain visible without key-color contamination; intentional outline/stroke is acceptable when it preserves the effect
- edges look anti-aliased at magnified scale, not stair-stepped
- subject is not clipped
- each final PNG came from its own source asset or a full-resolution per-element source, not from a cropped combined sheet
- Photopea processed outputs exist when upload-ready PNG elements were requested
- CSV basenames match final PNG basenames
- external DesignHub upload/submission was not performed unless the user explicitly confirmed it

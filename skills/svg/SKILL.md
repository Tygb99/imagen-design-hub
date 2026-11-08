---
name: svg
description: "Use for MiriCanvas or DesignHub SVG element work: simple vector illustrations, color-editable elements, SVG cleanup, validation, and SVG element CSV rows."
---

# Imagen Design Hub: SVG

[한국어](SKILL.ko.md)

Use this route when the user says `svg`, SVG element, vector element, color-changeable icon, simple flat sticker, extended element, memo note, speech bubble, flag, label, or reusable shape.

Treat outputs as candidates until validation and manual visual review pass.

Shared reference: read `../../SKILL.md` and `../../references/designhub-element-guide-map.md` when official file specs or type boundaries matter.

## Images 2.6 generation and edits

Check the selected tool's actual output formats. If it exposes real SVG generation, use that export and preserve the returned original before cleanup. When the user chooses built-in `image_gen` and it returns PNG, preserve that source and trace or rebuild it into real vector paths. Existing vectors, vector-editor exports and simple authored vectors remain valid inputs. Use the Images 2.6 API route only when the user explicitly selects it. Do not add invented native-tool arguments or silently switch to paid generation.

For native PNG tracing, request simple flat shapes with at most five visible colors, then use an available vectorizer/editor such as VTracer. Gradients, alpha halos and texture can create excess colors or speckles. A solid background can be removed as a vector shape after tracing when it is clearly separate from the subject; preserve the subject's own white regions and holes. Reduce the palette deliberately, inspect the vector against the PNG, then apply the normal outline, bounds and file checks below. Record this as native PNG generation followed by vector conversion, not direct SVG generation; report the backend model only when the tool identifies it.

On an explicitly selected API path, use `gpt-image-2.6-flare` or `gpt-image-2.6-sunburst` with `/v1/images/generations`, `output_format="svg"` and `n=1`; decode the returned base64 into UTF-8 SVG. See [controls and API restrictions](../../references/2026-11-06-22-36-21-images-2-6.md). A generated SVG is a candidate and still needs the finishing below. Edit an existing vector in its native source; SVG output is not supported by the image edit endpoint. If a raster preview is used as a reference, keep it separate from the final vector.

## Core Rules

- Use a true vector source: supported Images 2.6 SVG output, hand-authored SVG, vector-editor export, or traced/rebuilt vector art.
- Do not submit raster art renamed to `.svg`.
- Do not embed bitmap payloads as the main artwork.
- Keep the illustration simple with 5 or fewer visible colors across fills and strokes. Count white and black; exclude transparent and none values.
- Before upload, convert every visible stroke to a filled outline path. Preserve the shape and color, and remove all `stroke` and `stroke-*` attributes, including `stroke="none"`. DesignHub's uploader rejects SVG stroke attributes; do not discard visible borders to bypass the error.
- Remove rectangular artboards and background shapes unless the shape itself is the reusable element.
- Avoid scripts, external links, `foreignObject`, hidden watermarks, stray off-artboard objects, and text artifacts from unknown fonts.
- After outline conversion, compute the complete visible geometry bounds with the vector editor or the authored geometry. Set `viewBox` to those bounds and set width/height to the same aspect ratio. Preserve the artwork's shape, colors and outline thickness while trimming the original artboard's empty padding. Keep an original canvas only when the user explicitly requires that canvas size.

## Output Contract

- Final files are `.svg`.
- Maximum dimension is 6000 px.
- File size is under 0.15 MB.
- CSV rows use `contentType` value `SVG element`.
- Write CSV as UTF-8 without BOM using exactly `fileName,uniqueId,elementName,keywords,tier,contentType`; quote fields containing commas. This applies to local metadata preparation even when no upload is requested.
- CSV `fileName` is the basename only, without `.svg`.
- `uniqueId` stays blank unless it came from a DesignHub-downloaded CSV after upload.
- Keywords must be 20 to 25 unique buyer-facing terms.

## Validation

Before calling an SVG candidate ready:

- XML parses cleanly
- no embedded raster `<image>` payloads for the main artwork
- no scripts, external links, or `foreignObject`
- `viewBox` and dimensions are present and within limits
- imported/edited sources are cropped after outline conversion; all visible geometry fits inside the viewBox and no empty artboard padding remains
- visible colors are 5 or fewer
- all borders are filled outline paths, with no `stroke` or `stroke-*` attributes
- path quality and DesignHub suitability were checked by eye
- external DesignHub upload/submission was not performed unless the user explicitly confirmed it

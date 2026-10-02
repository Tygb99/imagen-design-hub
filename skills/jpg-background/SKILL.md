---
name: jpg-background
description: "Create DesignHub JPG graphic backgrounds and balanced patterns, check Background eligibility against Photo or subject elements, convert image_gen sources, and prepare Background CSV metadata."
---

# Imagen Design Hub: JPG Background

Use this route for `jpg배경`, DesignHub background JPGs, graphic document backgrounds, or repeat patterns. Classify the image by its content before choosing `Background`; a JPG extension alone does not establish eligibility.

[한국어](SKILL.ko.md). Shared workflow: [../../SKILL.md](../../SKILL.md).

## Review Eligibility

Checked 2026-10-02 KST against the official [Background guide](https://slashpage.com/designhub-guide/ndvwx728377exm3z6jpg) and [Photo type details](https://slashpage.com/designhub-guide/5r398nmnrxxd3mvwje7y). Recheck these pages before submission if requirements may have changed.

| Content | Route |
| --- | --- |
| Graphic illustration without a person, animal, or object as its subject | `Background`: for example, abstract curves, dots, or a graphic paper texture. |
| Harmonious pattern with no particular subject standing out | `Background`: recognizable repeated motifs are not automatically disallowed; inspect their balance and visual emphasis. |
| Real photograph or strongly photorealistic image, including scenery | `Photo`, subject to that type's own requirements. Water, a pool floor, paper, or light reflections are not automatically backgrounds. |
| Rectangular illustration with a focal person, animal, or object | Separate the objects into appropriate element types. If they cannot be separated, the illustration is unsupported; do not relabel it `Photo`. |

For a school notice, announcement, or poster batch, create the JPG as a separate graphic background layer. Keep the notice wording and focal illustrations out of that layer, even when text is allowed in the other requested formats. A finished notice layout does not become an eligible background by saving it as JPG.

## Generation and File Checks

1. Use built-in `image_gen` for an opaque, full-bleed rectangular or square graphic background or balanced pattern. Do not request cutouts or chroma key. Omit notice text, logos, watermarks, UI captures, and decorative frames from generated document backgrounds.
2. Preserve the source PNG and the authored prompt under the current run. Convert a separate copy to RGB `.jpg`; do not overwrite sources or failed candidates.
3. Check the actual JPEG signature, RGB mode, dimensions, DPI, file size, and visual eligibility. File validation alone does not establish content-type suitability or review approval.

The official [file specification](https://slashpage.com/designhub-guide/3p4kj92ynppxkm57q1x8) lists JPG, at least 120 DPI, 2500–9800 px, and a 50 MB maximum for Background. The local preparation target is 2500–9800 px on each side, under 50 MB, and 300 DPI unless the project overrides it. A project requirement such as 350 DPI is a local target, not the official minimum. Preserve aspect ratio when resizing.

## Metadata and Submission

- Use `fileName,uniqueId,elementName,keywords,tier,contentType`. A local preupload row uses the extensionless JPG basename, blank `uniqueId`, default `Premium`, and `Background` only for eligible images.
- Write 20–25 unique buyer-facing keywords describing the actual graphic or pattern. Do not label an abstract background as a finished school notice just because it was created in that batch.
- Local preupload Background rows must match the accepted JPG candidates. After upload, preserve every row, assigned ID, and filename spelling in DesignHub's downloaded CSV, including other formats; merge rather than discard those rows.
- For generated images, confirm the generative-AI checkbox before submission, including edited images, and retain prompt/source evidence as required by the official [AI guide](https://slashpage.com/designhub-guide/7vgjr4m1nqq8k2dwpy86).
- Use [upload-csv](../upload-csv/SKILL.md) for authorized uploads and review submissions. Existing authorization remains valid. Verify and report file upload, metadata processing, and review status separately; submission is not approval.

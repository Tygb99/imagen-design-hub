---
name: template-fit
description: Turn one keyword into a bundle of transparent PNG parts that buyers can drop into other people's MiriCanvas templates — edge panels, top bands, corner ornaments, open frames, bottom trims, scatter clusters and small single props — with shape, style, color, ratio and naming rules. Generation, finishing and upload follow png-element and upload-csv.
---

# Imagen Design Hub: Template-Fit Elements

[한국어](SKILL.ko.md)

Use when the user gives a keyword and wants elements that fit into templates made by others ("elements that suit other people's templates", "template parts", "decor for existing templates"). This route plans the bundle and adds the shape rules below. Generation, sources, finishing and preflight follow [png-element](../png-element/SKILL.md); upload and review submission happen only when requested, through [upload-csv](../upload-csv/SKILL.md).

## Why parts

A 2026-11-16 survey of 25 popular MiriCanvas templates (five keywords, top of the default search order) found decorative elements used as parts, not scenes: curtains attached to the left or right edge, swags across the top, wreaths and arches around the title, one small trophy or ribbon, confetti falling from the top. The template already paints its background, so an element must be a transparent fragment that leaves the text area open. Square, finished scenes had to be stretched and clashed with flat or photographic templates. [Survey and test record](../../records/2026-11-18-11-35-17-template-fit.md).

## Plan the bundle before generating

Inputs: the keyword, the count N (default 20 for a daily bundle; 3–5 for a sample) and any target template formats the user names.

1. Write a concept table first (for example `concepts.json`): part type, shape, style family, main and support colors, target aspect ratio and a Korean element name per item.
2. At least 60% of the items are part shapes (12 of 20, 3 of 5):
   - edge panel: vertical, hugging the left or right edge
   - top band: swag, garland or light string across the top
   - corner ornament
   - open frame with an empty center: wreath, arch, halo
   - bottom base or trim band
   - scatter cluster falling from the top: confetti, sparkles
   The rest are small single props. Never make a scene that fills the canvas.
3. Make mirrored pairs one side only; buyers flip them in MiriCanvas. Do not upload the left and right copies of the same shape as two items.
4. When the keyword is itself a frame or prop (for example a laurel wreath or a trophy), vary the part type around it: half wreath for a corner, wreath with an empty center, small sprig beside a title, garland band.

## Shape rules for every prompt

1. Transparent background. No text, numbers or logos inside the element. Do not cover the template's title or date area.
2. The side that meets the template edge may end in a straight line (outer edge of a panel, top edge of a band). The side facing the center stays open for text.
3. Use one of the two style families popular templates use: flat vector illustration with 2–4 solid fills, or photorealistic material (velvet, satin, metallic sheen). Textured crafts such as clay, felt, knit or paper craft stay at 10% or less of the bundle (2 of 20).
4. One main color and one or two support colors, chosen from mainstream template palettes: red or burgundy, black with gold, navy, ivory or beige, soft pastel. No ground shadow, background fragment or stage floor.
5. Keep the long side at most 2.5× the short side. Native image outputs vary in size (observed long sides about 1400–2200 px) and the tool may expose no size option, so a 3× band crops to a short side below 700 px and fails preflight (observed: `cropped size 572x1981: short side below 700px`; in the 2026-11-18 test three of four first attempts came back 2.9–4.6× and had to be regenerated). Make top bands 2–2.5× and keep hanging folds short; a 1.5× deep swag covered a poster title in the overlay test.
6. A simple silhouette that still reads when small; avoid heavy fine patterns. Keep the alpha of glow, halo and translucent fabric, but the preflight margin check must still pass.
7. Put the use in the element name and keywords: frame, border, corner ornament, top decoration, edge decoration, band (in Korean metadata: 테두리, 프레임, 구석 장식, 상단 장식, 가장자리 장식, 띠).

## Make and check

1. Generate one source per element with the native tool following png-element, preserve sources, finish copies, then crop and run the margin preflight.
2. Check the ratio from this plugin's root right after cropping each source, before resizing, and again on the finals:
   `python3 scripts/designhub_preflight.py ratio --max-ratio 2.5 <cropped-or-final.png> ...`
   FAIL exits non-zero; regenerate a less elongated version. Do not stretch, squash or pad a failing crop to pass. Proportional resizing of a passing crop to the final size is normal finishing.
3. Inspect every final on light and dark backgrounds. Count part types against the plan and confirm the style family, color count, no text and an open center for frames.
4. When fit is in doubt, place the element on a simple template mock-up (for example a 1080×1528 poster with a title box and a date line, mirrored copies for edge pairs) and judge whether the title and date stay readable. Report which items fit and which did not, with the reason.
5. Report the concept table with measured sizes, ratios, part-type counts and the paths of sources, finals and previews.

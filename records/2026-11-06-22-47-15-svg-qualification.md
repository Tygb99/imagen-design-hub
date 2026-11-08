# SVG skill qualification — 0.9.0

[한국어](2026-11-06-22-47-15-svg-qualification.ko.md) · [Measured evidence](2026-11-06-22-47-15-svg-qualification.json)

**PASS for local SVG authoring/editing and metadata preparation.** Images 2.6 API SVG generation and live DesignHub upload, registration or review were not executed. The stable skill name is `imagen-design-hub:svg`.

## Target and contract

- Skill root in each fresh package: `plugin/skills/svg/`.
- Distribution: exactly the entries in `package.json` `files`, copied into separate directories without Git history, original workspace access or prior-run artifacts. Bundled SVG/shared/keyword/upload guidance was available.
- Representative request: make a flat flower, preserve the supplied outlined round badge, and make a blank speech bubble; retain originals and prepare Korean metadata.
- Source: `input/round-badge.svg`, a 1024×1024 SVG with a radius-400 circle at (512,512), white fill and a 48-unit dark outline.
- Search boundary: `input/`, depth 1, `*.svg`, filename order, no symlink following. All other input roots excluded.
- Required outputs: three final SVGs, `sources/`, `preupload.csv`, `result.json` and `missing-input.json` under `output/`.
- Allowed variation: new flower/bubble geometry, colors, valid keyword wording/count within 20–25, and run paths/times. Source selection, route, order, output structure and acceptance decision must agree.
- PASS: true vectors, at most five colors, no stroke attributes, preserved outline, tight complete bounds, maximum 6000px, under 150000 bytes, exact six-column UTF-8 CSV without BOM, blank IDs and correct content type.

## Static inspection

| Reference or dependency | Availability | Check |
| --- | --- | --- |
| SVG and shared skills | Included | Actual paths read by both executions |
| File-type and keyword guides | Included | Relative references resolve |
| `svg-outline-crop.json` regression input | Included in eval fixtures | Original geometry and expected bounds recorded |
| Python/Node | User-provided runtime, documented in README | Local vector authoring used no image/API service |
| `sharp` | Verification environment only | Rendered previews, alpha bounds and outline comparison; not required by the skill |

Seven skill entrypoints and agent YAML pass format checks. Active links resolve to `skills/svg/`; historical changelog entries retain the old name. Installation is documented in README (install, version check, new-chat activation and removal). The installed 0.9.0 package was separately discovered through `$imagen-design-hub:svg`; the read-only activation test returned the exact tight-viewBox and BOM-free CSV requirements.

## Test 1: cold acceptance

Fresh directory: `final-1/` in artifact set `svg-verification-2026-11-06-22-30-28`. Only packaged files and the source were copied. Executed the command below with the representative request; process exited 0.

```sh
codex --ask-for-approval never exec --ignore-user-config --skip-git-repo-check --ephemeral --sandbox workspace-write --json -o last-message.txt - < prompt.txt
```

Produced all requested files. Inspected final renders and checked the actual vector/CSV files. Missing `input/missing-character.svg` returned a missing-input result without fabricating a character. Route: `local-vector`. Input: only `input/round-badge.svg`. Output order: flower, round-badge, speech-bubble. Keywords: 20 per asset. **PASS.**

## Test 2: independent repeat

Fresh directory: `final-2/`; no state from test 1 reused. Identical package, source, request and command; process exited 0. Same source selection, local-vector route, ordering, output structure and missing-input decision. Keywords: 22 per asset, within the allowed range. **PASS.**

| Run | File | Bytes | Colors | Alpha margins (L,T,R,B) |
| --- | --- | ---: | ---: | --- |
| final-1 | flower.svg | 465 | 3 | 0,0,0,0 |
| final-1 | round-badge.svg | 228 | 2 | 0,0,0,0 |
| final-1 | speech-bubble.svg | 383 | 2 | 0,0,0,0 |
| final-2 | flower.svg | 476 | 3 | 0,0,0,0 |
| final-2 | round-badge.svg | 298 | 2 | 0,0,0,0 |
| final-2 | speech-bubble.svg | 325 | 2 | 0,0,0,0 |

At 848×848 comparison size, badge mean absolute RGBA differences from the original outline render were 0.00853 and 0.08553 on the 0–255 scale (limit 1). All preview margins were 0px. Visual review found no clipping, missing borders or unexpected raster content.

## Negative checks

Rejected all 11 mutated inputs: malformed XML, raster image, script, foreignObject, external link, stroke=none, six colors, over-6000px dimensions, over-size file, missing viewBox and an external entity. The acceptance checker handles group fill inheritance. It is a flat-vector test checker, not a complete SVG specification validator.

## Defects and corrections

| Defect | Observed evidence | Correction | Retest |
| --- | --- | --- | --- |
| Original artboard padding remained after editing | Both first `svg` runs retained 1024×1024; 44px margin at 512px preview size | Require visible bounds after outline conversion; preserve artwork while trimming the artboard | Both final runs export the badge at tight 848×848 bounds |
| Local CSV encoding varied | One intermediate run wrote an EF BB BF BOM | State exact header and UTF-8 without BOM directly in SVG output requirements | Both final CSVs pass exact header/encoding checks |

The checker was also corrected to respect group fill inheritance and equivalent underscore/hyphen spelling in missing-input statuses; these were test-harness assumptions, not SVG defects. Every skill correction was followed by two new complete executions.

## Final decision

**PASS within the declared local scope.** Both fresh executions, source isolation, repeat agreement, visual review, 11 negative rejections and installed-skill discovery have actual evidence. Promote the route to `svg` in 0.9.0. External API behavior and DesignHub acceptance remain unverified; no public release or approval is claimed.

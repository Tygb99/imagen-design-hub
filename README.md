# imagen-design-hub 0.9.0

[한국어](README.ko.md) · [Changelog](2026-11-13-22-10-33-CHANGELOG.md)

Recommend useful PNG elements and create native transparent assets with Codex, following Images 2.6 generation and editing guidance. Finish dimensions and DPI locally, prepare DesignHub metadata, and organize approved public elements into collections.

## Routes

- PNG recommendations and native transparency: [png-element](skills/png-element/SKILL.md).
- Animated GIF candidates: [gif](skills/gif/SKILL.md), following the installed sprite-gen version.
- Graphic backgrounds and balanced patterns: [jpg-background](skills/jpg-background/SKILL.md), with official Background/Photo type checks.
- True vector elements: [svg](skills/svg/SKILL.md).
- Aside upload and CSV roundtrip: [upload-csv](skills/upload-csv/SKILL.md), using `setInputFiles()` first and the native file picker as fallback.
- Collections: [collection](skills/collection/SKILL.md), for current limits, existing membership, eligible groups, names/keywords, registration, and saved-state checks.

## Version 0.9.0

Promoted `svg-beta` to `svg` after local vector-production acceptance testing. Use `$imagen-design-hub:svg`. Added SVG agent metadata and kept the same vector, color, outline, file and metadata checks. A separate live test used built-in image_gen, converted its PNG into a four-color SVG, uploaded one file, processed all 101 CSV rows, saved the AI flag and submitted that one item for review. A DesignHub screenshot reviewed on 2026-11-13 confirmed that the same SVG was approved, with its Premium license and generative AI label retained. The user selected the native tool, so the API route was not run and the backend model was not identified by the tool.

[SVG qualification report](records/2026-11-06-22-47-15-svg-qualification.md) · [Native generation and DesignHub approval](records/2026-11-13-22-10-33-native-svg-live.md)

## Version 0.8.0

Updated PNG/JPG generation, reference edits and SVG guidance against [Images 2.6](https://openai.com/index/introducing-images-2-6/). Preserve subject identity and alpha across edits; reuse an accepted reference for variants. [Images 2.6 controls](references/2026-11-06-22-36-21-images-2-6.md) covers optional API quality/complexity, markup and SVG export. Check the actual tool schema: API support does not imply the native Codex tool exposes those options, and the plugin adds no API client. GIF stays on sprite-gen. Free-plan diagnostics and DesignHub submission checks continue to apply.

## Version 0.7.0

Added the `collection` skill in English and Korean. It groups approved public elements by type and theme, balances groups within the live limits, preserves identifiers, avoids existing memberships and duplicate retries, and records saved collections separately from element CSV metadata. It also supports requested name/keyword edits through the existing collection.

Example: “Use $imagen-design-hub:collection to organize my approved public elements into collections with Korean names and 25 keywords.”

## Version 0.6.2

After 12 DesignHub rejections, added `scripts/designhub_preflight.py`: GIF all-frame crop with a 700 px recheck, a zero-margin PNG/GIF alpha check (alpha ≤ 8/255 counts as empty), and an upload stop for names in `records/designhub-rejected-elements.csv`; GIFs with only simple motion now need user confirmation.

## Version 0.6.1

Updated JPG guidance against the official [Background guide](https://slashpage.com/designhub-guide/ndvwx728377exm3z6jpg): use subjectless graphics or harmonious patterns with no standout subject. Route photographs and strongly photorealistic images to Photo; separate focal illustrations into elements instead of submitting a finished poster as Background. JPG conversion does not fix a type mismatch.

The JPG skill now distinguishes official file limits from local DPI targets, preserves downloaded CSV rows and IDs, and verifies the generative-AI flag for generated submissions. Replaced conflicting natural/photorealistic-background guidance in the routes, reference map, landing page, and evaluation cases.

Native transparent image_gen is the PNG default. Preserve intentional partial alpha and source files; use Pillow or an existing local processor for trim, dimensions and DPI.

GIF uses sprite-gen's own component-row generation and extraction. Its current row contract still uses chroma sources. GIF has binary transparency and a limited palette, so glass translucency cannot match RGBA PNG exactly. Keep original frames and inspect actual motion before reporting success.

[Images 2.6 announcement](https://openai.com/index/introducing-images-2-6/) is the current generation and editing baseline. Record the actual model/version/variant only when the tool identifies it.

## Install or update

Codex CLI must already run in the terminal used below. Installing the desktop app or this plugin does not guarantee a `codex` command on PATH. On Windows, check `Get-Command codex -All` and `codex --version` first. See [image-generation diagnostics](references/image-generation-troubleshooting.md) for Windows setup and missing-tool recovery.

Clone the repository at the personal marketplace's expected path, then register and install it:

```sh
git clone https://github.com/Tygb99/imagen-design-hub.git "$HOME/plugins/imagen-design-hub"
node "$HOME/plugins/imagen-design-hub/scripts/register_marketplace.mjs"
codex plugin list
codex plugin add imagen-design-hub@<marketplace-name-shown-by-list>
```

If `codex plugin list` shows no local marketplace, run `codex plugin marketplace add "$HOME"` once, then list again.

For an already registered local plugin, update the source, then reinstall with Codex using the marketplace name shown by `codex plugin list`. This machine uses:

```sh
codex plugin add imagen-design-hub@tygb99-personal
```

Verify the listed version is 0.9.0 and start a new task after reinstall to load updated skills. To remove the plugin, run `codex plugin remove imagen-design-hub@<marketplace-name>` and then `node "$HOME/plugins/imagen-design-hub/scripts/unregister_marketplace.mjs"`. No npm package installation is required. The existing auto-update script only fast-forwards clean source checkouts; local edits are preserved. A local edit/reinstall is not a public release or GitHub push.

## Dependencies

- A Codex session exposing its native image tool with an eligible ChatGPT sign-in; no API key is required for that native path. Codex image generation is not available on the Free plan. Plugin installation alone does not enable it; see [requirements and diagnostics](references/image-generation-troubleshooting.md).
- Python and Pillow for local finishing.
- Installed sprite-gen and its own venv for GIFs; follow its versioned SKILL.md.
- Aside REPL for DesignHub operations; Computer Use for native file-picker fallback when needed.
- Node 18+ and Git for installer/update scripts.

Read [the workflow](SKILL.md), [keyword guidance](references/keyword-generation.md), and [format guide](references/designhub-element-guide-map.md). Keep originals and write derived outputs separately. Upload filenames and downloaded uniqueId values must remain aligned.

MIT license: [LICENSE](LICENSE).

# imagen-design-hub 0.5.0

[한국어](README.ko.md)

Recommend useful PNG elements and create native transparent assets with Codex. Finish dimensions and DPI locally, inspect alpha, and prepare DesignHub metadata.

## Routes

- PNG recommendations and native transparency: [png-element](skills/png-element/SKILL.md).
- Animated GIF candidates: [gif-beta](skills/gif-beta/SKILL.md), using installed sprite-gen 2.0.3.
- Full-bleed backgrounds: [jpg-background](skills/jpg-background/SKILL.md).
- True vector elements: [svg-beta](skills/svg-beta/SKILL.md).
- Computer Use upload and CSV roundtrip: [upload-csv](skills/upload-csv/SKILL.md).

## Version 0.5.0

Native transparent image_gen is the PNG default. Mandatory chroma keying, blanket fringe cleanup and the separate Aside transparency skill have been removed. Preserve intentional partial alpha; inspect checkerboard, white and dark previews. Photopea is optional, and its runner remains for manual editing workflows.

GIF uses sprite-gen's own component-row generation and extraction. Its current row contract still uses chroma sources. GIF has binary transparency and a limited palette, so glass translucency cannot match RGBA PNG exactly. Keep original frames and inspect actual motion before reporting success.

[Images 2.5 announcement](https://openai.com/index/introducing-chatgpt-images-2-5/) confirms Codex and transparent-background support. Exact backend model variants must not be inferred from tool availability.

## Install or update

Clone this repository to your plugin directory and register its local marketplace with the supplied installer:

```sh
git clone https://github.com/Tygb99/imagen-design-hub.git
cd imagen-design-hub
node scripts/register_marketplace.mjs
```

For an already registered local plugin, update the source, then reinstall with Codex using the marketplace name returned by your personal marketplace. This machine uses:

```sh
codex plugin add imagen-design-hub@tygb99-personal
```

Start a new task after reinstall to load updated skills. No npm package installation is required. The existing auto-update script only fast-forwards clean source checkouts; local edits are preserved. A local edit/reinstall is not a public release or GitHub push.

## Dependencies

- Codex built-in image_gen for PNG generation; no API key required.
- Python and Pillow for local finishing.
- Installed sprite-gen and its own venv for GIFs; follow its versioned SKILL.md.
- Computer Use for live DesignHub operations.
- Node 18+ and Git for installer/update scripts.
- Photopea only when manual editing is needed or requested.

Read [the workflow](SKILL.md), [keyword guidance](references/keyword-generation.md), and [format guide](references/designhub-element-guide-map.md). Keep originals and write derived outputs separately. Upload filenames and downloaded uniqueId values must remain aligned.

MIT license: [LICENSE](LICENSE).

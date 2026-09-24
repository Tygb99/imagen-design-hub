# imagen-design-hub 0.5.1

[한국어](README.ko.md)

Recommend useful PNG elements and create native transparent assets with Codex. Finish dimensions and DPI locally, inspect alpha, and prepare DesignHub metadata.

## Routes

- PNG recommendations and native transparency: [png-element](skills/png-element/SKILL.md).
- Animated GIF candidates: [gif](skills/gif/SKILL.md), integration verified with sprite-gen 2.7.0.
- Full-bleed backgrounds: [jpg-background](skills/jpg-background/SKILL.md).
- True vector elements: [svg-beta](skills/svg-beta/SKILL.md).
- Computer Use upload and CSV roundtrip: [upload-csv](skills/upload-csv/SKILL.md).

## Version 0.5.1

The GIF route is now `gif` (no beta suffix). The documented sprite-gen row pipeline is verified against 2.7.0. The 0.5.0 native transparent PNG workflow remains the default for PNG elements.

Native transparent image_gen is the PNG default. Mandatory chroma keying, blanket fringe cleanup and the separate Aside transparency skill have been removed. Preserve intentional partial alpha; inspect checkerboard, white and dark previews. Photopea is optional, and its runner remains for manual editing workflows.

GIF uses sprite-gen's own component-row generation and extraction. Its current row contract still uses chroma sources. GIF has binary transparency and a limited palette, so glass translucency cannot match RGBA PNG exactly. Keep original frames and inspect actual motion before reporting success.

[Images 2.5 announcement](https://openai.com/index/introducing-chatgpt-images-2-5/) confirms Codex and transparent-background support. Exact backend model variants must not be inferred from tool availability.

## Install or update

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

Verify the listed version is 0.5.1 and start a new task after reinstall to load updated skills. To remove the plugin, run `codex plugin remove imagen-design-hub@<marketplace-name>` and then `node "$HOME/plugins/imagen-design-hub/scripts/unregister_marketplace.mjs"`. No npm package installation is required. The existing auto-update script only fast-forwards clean source checkouts; local edits are preserved. A local edit/reinstall is not a public release or GitHub push.

## Dependencies

- Codex built-in image_gen for PNG generation; no API key required.
- Python and Pillow for local finishing.
- Installed sprite-gen and its own venv for GIFs; follow its versioned SKILL.md.
- Computer Use for live DesignHub operations.
- Node 18+ and Git for installer/update scripts.
- Photopea only when manual editing is needed or requested.

Read [the workflow](SKILL.md), [keyword guidance](references/keyword-generation.md), and [format guide](references/designhub-element-guide-map.md). Keep originals and write derived outputs separately. Upload filenames and downloaded uniqueId values must remain aligned.

MIT license: [LICENSE](LICENSE).

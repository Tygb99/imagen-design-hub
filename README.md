# imagen-design-hub 0.6.0

[한국어](README.ko.md)

Recommend useful PNG elements and create native transparent assets with Codex. Finish dimensions and DPI locally and prepare DesignHub metadata.

## Routes

- PNG recommendations and native transparency: [png-element](skills/png-element/SKILL.md).
- Animated GIF candidates: [gif](skills/gif/SKILL.md), following the installed sprite-gen version.
- Full-bleed backgrounds: [jpg-background](skills/jpg-background/SKILL.md).
- True vector elements: [svg-beta](skills/svg-beta/SKILL.md).
- Aside upload and CSV roundtrip: [upload-csv](skills/upload-csv/SKILL.md), using `setInputFiles()` first and the native file picker as fallback.

## Version 0.6.0

Removed the retired browser editor and its runner. Generate native transparent PNGs with image_gen, then trim, resize and save DPI with Pillow or an existing local processor. GIFs follow the installed sprite-gen version and its own environment.

Native transparent image_gen is the PNG default. Preserve intentional partial alpha and source files.

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

Verify the listed version is 0.6.0 and start a new task after reinstall to load updated skills. To remove the plugin, run `codex plugin remove imagen-design-hub@<marketplace-name>` and then `node "$HOME/plugins/imagen-design-hub/scripts/unregister_marketplace.mjs"`. No npm package installation is required. The existing auto-update script only fast-forwards clean source checkouts; local edits are preserved. A local edit/reinstall is not a public release or GitHub push.

## Dependencies

- Codex built-in image_gen for PNG generation; no API key required.
- Python and Pillow for local finishing.
- Installed sprite-gen and its own venv for GIFs; follow its versioned SKILL.md.
- Aside REPL for DesignHub operations; Computer Use for native file-picker fallback when needed.
- Node 18+ and Git for installer/update scripts.

Read [the workflow](SKILL.md), [keyword guidance](references/keyword-generation.md), and [format guide](references/designhub-element-guide-map.md). Keep originals and write derived outputs separately. Upload filenames and downloaded uniqueId values must remain aligned.

MIT license: [LICENSE](LICENSE).

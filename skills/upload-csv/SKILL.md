---
name: upload-csv
description: Use after MiriCanvas or DesignHub element files are ready for upload and the next step requires a live DesignHub surface such as Aside on macOS, MCP when available, or an explicitly confirmed UI route to upload files, download CSV metadata, preserve uniqueId values, merge rows, and re-upload the CSV.
---

# Imagen Design Hub: Upload Then CSV

[Korean version](SKILL.ko.md)

Use this route when the user says `요소 업로드후 csv업로드`, `uplode-csv`, `upload-csv`, DesignHub upload CSV, metadata upload, CSV merge, uniqueId preservation, or post-upload DesignHub metadata.

This skill is for the post-file-upload metadata phase. It should not silently submit a DesignHub review.

Shared reference: read `../../SKILL.md` for route-specific `contentType` values and keyword rules.

## Mandatory Live Surface

Any live DesignHub UI action in this route must use the surface the user requested.

- If the user asks for Aside, use `aside-browser`. Aside is currently supported on macOS only; Windows support is planned, so do not claim or assume Windows Aside support.
- The next preferred automation route is MCP. If DesignHub MCP tools are available and the user asks for them, use MCP for upload/download actions instead of a browser UI route.
- Do not switch to Chrome, Computer Use, hidden browser automation, direct HTTP calls, hidden APIs, or terminal-only shortcuts after the user names another surface.
- Use Chrome or Computer Use only when the user explicitly asks for it, or when no specific surface was requested and that route is the confirmed supported path.
- Local CSV merging, row validation, encoding checks, and file inspections may still use normal filesystem and terminal tools.
- Uploading files and transmitting CSV metadata to DesignHub require explicit user confirmation before the live action if that confirmation has not already been provided for the specific files and destination.
- Never click final review submission unless the user explicitly asks for that separate external submission step.

## Required Sequence

1. Use the confirmed live surface to upload the prepared image/vector/GIF files only when the user has explicitly confirmed the external DesignHub action.
2. Wait for DesignHub's upload completion state, such as `10 of 10 uploaded`, before treating the upload as complete.
3. Use the same confirmed live surface to download the CSV provided by DesignHub after file upload.
4. Treat the downloaded CSV as the source of truth for `fileName` and `uniqueId`.
5. Merge prepared metadata into the downloaded rows without dropping, reordering unnecessarily, or regenerating `uniqueId`.
6. Keep every row from the downloaded DesignHub CSV, not just the new batch rows.
7. Keep the CSV UTF-8 without BOM and quote all fields when the local project contract requires quote-all CSV.
8. Use the confirmed live surface to re-upload the merged CSV only when the user has explicitly confirmed that external action.
9. Verify the DesignHub completion message or banner after CSV upload. Record the processed row count, and distinguish file upload, CSV upload, and final review submission.

Do not upload a local preupload CSV directly after files are registered. DesignHub assigns `uniqueId` values only after the file upload, so the correct flow is always download the current DesignHub CSV, merge into that full file, and upload the merged full CSV.

## Content Type Values

Use the official CSV values exactly:

```text
Photo
Photo(Cut-out)
SVG element
PNG element
GIF
Background
```

Do not write `JPG background`; use `Background`.

## Metadata Rules

- `fileName` is usually extensionless for JPG backgrounds, SVG, and GIF rows.
- For PNG element flows, match whatever DesignHub's downloaded CSV expects and keep the final upload basename aligned with the actual file.
- `uniqueId` must be preserved from the downloaded DesignHub CSV.
- `tier` defaults to `Premium` unless the user says otherwise.
- `keywords` must be 20 to 25 unique buyer-facing terms.
- Remove production/admin terms such as `Photopea`, `imagegen`, `PNG`, `JPG`, `SVG`, `GIF`, `CSV`, `Premium`, `DesignHub`, `MiriCanvas`, run IDs, and dates unless the user explicitly requires one.

## Validation

Before reporting ready:

- row count matches DesignHub's downloaded CSV
- all `uniqueId` values from the downloaded CSV are preserved
- all final `fileName` values map to uploaded files
- the merged CSV keeps every row from the downloaded DesignHub CSV, not just the new batch rows
- `contentType` values are from the official list
- no duplicate keywords remain within each row
- keyword counts are 20 to 25 per row
- CSV encoding is UTF-8 without BOM
- every field is quoted if the local project contract requires quote-all CSV
- live DesignHub file upload, CSV download, and CSV upload were performed through the user-requested surface
- Aside use was limited to macOS, or MCP/another supported route was explicitly selected
- DesignHub displayed a successful processed-row count or an error message was captured verbatim
- DesignHub reported the expected upload count and CSV processed-row count
- state clearly whether file upload, CSV upload, or final review submission actually happened

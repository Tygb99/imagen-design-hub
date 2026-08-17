---
name: upload-csv
description: Use after MiriCanvas or DesignHub element files are ready for upload and the next step requires Computer Use to operate the live DesignHub surface for file upload, CSV metadata download, uniqueId preservation, metadata merge, and merged CSV re-upload.
---

# Imagen Design Hub: Upload Then CSV

[Korean version](SKILL.ko.md)

Use this route when the user says `요소 업로드후 csv업로드`, `uplode-csv`, `upload-csv`, DesignHub upload CSV, metadata upload, CSV merge, uniqueId preservation, or post-upload DesignHub metadata.

This skill is for the post-file-upload metadata phase. It should not silently submit a DesignHub review.

Shared reference: read `../../SKILL.md` for route-specific `contentType` values and keyword rules.

## Mandatory Live Surface

Every live DesignHub UI action in this route must use Computer Use.

- Use Computer Use for the DesignHub page, file upload controls, CSV download controls, macOS file picker/file explorer, and CSV re-upload controls.
- Do not use MCP, Aside MCP CLI, `aside-browser`, Chrome-only automation, hidden browser automation, direct HTTP calls, hidden APIs, or terminal-only shortcuts for the live DesignHub actions in this route.
- Local CSV merging, row validation, encoding checks, and file inspections may still use normal filesystem and terminal tools.
- Uploading files and transmitting CSV metadata to DesignHub require explicit user confirmation before the live action if that confirmation has not already been provided for the specific files and destination.
- Never click final review submission unless the user explicitly asks for that separate external submission step.

## Required Sequence

1. Use the confirmed live surface to upload the prepared image/vector/GIF files only when the user has explicitly confirmed the external DesignHub action.
2. Wait for DesignHub's upload completion state, such as `10 of 10 uploaded`, before treating the upload as complete.
3. Navigate to the relevant pending/submission list and use its CSV download control after file upload. Do not assume the manage-page "all uploaded content" export contains pending files.
4. Complete any macOS save dialog with an explicit timestamped filename, then inspect the saved CSV locally.
5. Treat the downloaded CSV as the source of truth for `fileName` and `uniqueId` only after confirming that every newly uploaded basename is present and has a non-empty `uniqueId`.
6. Merge prepared metadata into the downloaded rows without dropping, reordering unnecessarily, or regenerating `uniqueId`.
7. Keep every row from the downloaded DesignHub CSV, not just the new batch rows.
8. Keep the CSV UTF-8 without BOM and quote all fields when the local project contract requires quote-all CSV.
9. Use the confirmed live surface to re-upload the merged CSV only when the user has explicitly confirmed that external action.
10. Verify the DesignHub completion message or banner after CSV upload. Record the processed row count, and distinguish file upload, CSV upload, and final review submission.

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
- live DesignHub file upload, CSV download, and CSV upload were all performed through Computer Use, including macOS file-picker/file-explorer steps
- MCP and Aside were not used for the live DesignHub actions in this route
- DesignHub displayed a successful processed-row count or an error message was captured verbatim
- DesignHub reported the expected upload count and CSV processed-row count
- state clearly whether file upload, CSV upload, or final review submission actually happened

## Operational Traps

The 2026-08-17 run exposed these failure modes:

- The manage-page "all uploaded content" CSV contained only active/manage rows (189 in that run). The submission-list `CSV를 다운로드` export contained the pending full set (275 rows) and the four newly uploaded basenames. Always verify that the chosen export contains every new basename and that its row count matches the target submission list.
- A DesignHub CSV download can open a macOS Save dialog. A `.com.google.Chrome.*` temporary file may be a readable CSV but is not the final saved artifact. Complete the Save dialog with a timestamped filename, then locate and inspect the saved file.
- The macOS picker can appear under Finder-like or Chrome `열기` state. Re-query the active app after each transition. Use Go To Folder to reach the exact directory or file, verify the target filename is selected and the Open button is enabled, and do not rely on blind `Cmd+A`; it can select folders or do nothing.
- A successful file upload or 275-row CSV processing banner is not approval. Background JPGs with visible subjects can still fail the Background review rule. Keep file upload, CSV processing, and final review submission as separate reported states.

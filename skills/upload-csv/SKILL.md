---
name: upload-csv
description: Upload prepared DesignHub assets or process existing pending items through Aside, preserve assigned uniqueId values during CSV metadata registration, and submit for review when authorized.
---

# Imagen Design Hub: Upload Then CSV

[Korean version](SKILL.ko.md)

Use this route when the user says `요소 업로드후 csv업로드`, `uplode-csv`, `upload-csv`, DesignHub upload CSV, metadata upload, CSV merge, uniqueId preservation, or post-upload DesignHub metadata.

Start with prepared files or the user's existing pending items. Upload, metadata registration, and review submission each require authorization covering the selected items and destination; existing authorization remains valid.

Shared reference: read `../../SKILL.md` for route-specific `contentType` values and keyword rules.

## Browser and file selection

- Prefer Aside REPL for DesignHub. Read the installed Aside skill and its current guide before use, attach the relevant existing tab, and inspect the current page to identify controls.
- Prefer the observed file-input locator's `setInputFiles()` for image/vector/GIF files and merged CSVs. For large batches, target 1,000 file paths per batch, reducing the batch to the live upload limit or a lower user-requested size. This is an operational batch size, not a claim about DesignHub's maximum.
- If direct file selection is unavailable or fails, use the browser's native file picker through Computer Use. Recheck selection before pressing Open. Do not switch browsers unless needed and consistent with the user's choice.
- Use browser download handling for CSV exports; complete a native save dialog through Computer Use only when one appears. Verify the completed download before merging.
- Local CSV merging and file checks may use filesystem tools. Function availability and file selection do not prove that DesignHub accepted the upload; verify its completion state.
- Retry failed items at most twice after the initial attempt, then skip them and continue. If an upload or submission response is unclear, inspect current state before retrying to avoid duplicates.

## Required Sequence

1. Confirm the target files or existing pending items and the authorized actions. Upload prepared files through Aside; skip file upload when processing items already registered on DesignHub. Keep unrelated items outside the selection.
2. For new uploads, wait for DesignHub's upload completion state, such as `10 of 10 uploaded`, before treating the upload as complete.
3. Navigate to the relevant pending/submission list and use its CSV download control. Do not assume the manage-page "all uploaded content" export contains pending files.
4. Verify the completed CSV download and inspect it locally. If a save dialog appears, save with an explicit timestamped filename.
5. Treat the downloaded CSV as the source of truth for `fileName` and `uniqueId` only after confirming that every newly uploaded basename is present and has a non-empty `uniqueId`.
6. Merge prepared metadata into the downloaded rows without dropping, reordering unnecessarily, or regenerating `uniqueId`.
7. Keep every row from the downloaded DesignHub CSV, not just the new batch rows.
8. Keep the CSV UTF-8 without BOM and quote all fields when the local project contract requires quote-all CSV.
9. Re-upload the merged CSV through Aside within the existing authorization. Do not repeat an approval request already covering these items and this destination.
10. Verify the DesignHub completion message or banner after CSV upload. Record the processed row count, and distinguish file upload, CSV upload, and final review submission.
11. Check the generative-AI flag for AI-generated assets and save it without overwriting individual names or keywords. Verify the saved state.
12. When review submission is authorized, submit only the intended items in groups allowed by the current page. Verify that they moved from pending to review waiting. File-selection batch size does not determine review capacity.

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
- Remove production/admin terms such as `imagegen`, `PNG`, `JPG`, `SVG`, `GIF`, `CSV`, `Premium`, `DesignHub`, `MiriCanvas`, run IDs, and dates unless the user explicitly requires one.

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
- the selected files, assigned IDs, and destination match the authorized batch
- the generative-AI flag was saved for AI-generated assets
- DesignHub displayed a successful processed-row count or an error message was captured verbatim
- DesignHub reported the expected upload count and CSV processed-row count
- state clearly whether file upload, CSV upload, or final review submission actually happened

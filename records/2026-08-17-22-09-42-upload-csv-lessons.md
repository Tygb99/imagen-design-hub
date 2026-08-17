# Upload CSV Lessons From the 2026-08-17 Run

This record captures the operational traps found while uploading four JPG backgrounds and registering a full DesignHub CSV.

## Observed sequence

- Four JPG files uploaded successfully through the DesignHub Background route.
- The manage-page all-uploaded export produced 189 active/manage rows and did not contain the new pending basenames.
- The submission-list CSV download produced 275 rows and contained all four new basenames with non-empty `uniqueId` values.
- The merged CSV preserved all 275 rows and all 275 `uniqueId` values. DesignHub reported: `모든 행(275행)을 처리했습니다.`
- Final review submission was intentionally not performed.

## Traps and fixes

1. Choose the CSV export from the pending/submission list, not merely the manage page. Match its row count to the target list and confirm every new basename is present.
2. Finish the macOS Save dialog after starting a CSV download. Treat `.com.google.Chrome.*` files as temporary until the named file is saved and locally inspected.
3. Re-query the active Computer Use app after the file picker changes between Finder-like and Chrome `열기` states.
4. Use Go To Folder with an exact directory or file path. Verify the target filename is selected and the Open button is enabled; blind `Cmd+A` is unreliable in this picker.
5. A successful upload and CSV processing banner do not mean review approval. Visible subjects may violate the Background policy even when the content type is `Background`.

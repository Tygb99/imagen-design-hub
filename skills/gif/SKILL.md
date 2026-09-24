---
name: gif
description: Create DesignHub GIF candidates through the installed sprite-gen component-row pipeline, motion QA and GIF metadata.
---

# GIF with sprite-gen

[Korean](SKILL.ko.md)

Read the installed sprite-gen SKILL.md and resolve its actual path. Integration verified against 2.7.0; consult its current docs before use. Do not copy the engine or assume a developer's home path.

Follow sprite-gen's user-workflow guide with choices already stated by the user. For this Codex workflow, select GPT rows and pass `--provider codex` explicitly. Use Grok video only when that route is requested; never switch to billed API generation automatically or save defaults without consent.

1. Inspect and lock a complete base. Prepare a new run with short readable states. For smooth glass illustration, disable pixel-unfake.
2. Use sprite-gen's venv and request-generated prompts: prepare → gen-set --provider codex → extract → compose-atlas → compose-gif → inspect. Version 2.7.0 rows still require chroma-key sources and omit --transparent; native PNG support does not change that contract. Take concurrency from the installed CLI.
3. Generate through Codex with the request's frame count, references, spacing and subject-safe key. Never substitute duplicated stills or locally drawn motion.
4. Preserve raw rows, frames, atlas, runtime manifest, GIF and QA reports. Compose through run-dir so curation is honored.
5. Inspect every frame and actual playback: motion, identity, scale, clipping, loop seam and ghosting. Regenerate a failing row.
6. Deliver verified files first. Curation is optional: open the Korean view when requested or already selected, then provide its URL.

When using sprite-gen gen for a separate transparent still or reference edit, pass `--provider codex --transparent --alpha-mode native`. Its auto strategy can choose chroma when references are attached; preserve glass alpha by selecting native explicitly. This still-image setting does not apply to animation rows.

GIF has palette-limited color and binary transparency; it cannot preserve PNG's continuous partial alpha. Keep RGBA sources and report glass-translucency loss. The image model generates still frames, not a native animated GIF.

Check hardware encoding support first. If there is no hardware GIF palette/LZW encoder, use sprite-gen's CPU writer and state why.

Verify real animated GIF, multiple distinct frames, intended looping, 700–1920 px per side, under 25 MB, and checkerboard/white/dark playback. Confirm current official DesignHub acceptance rules before submission.

CSV: extensionless fileName, contentType GIF, default tier Premium, 20–25 unique buyer-facing keywords, and no invented uniqueId. Follow [shared rules](../../SKILL.md) and [upload-csv](../upload-csv/SKILL.md). Report candidate quality separately from upload/review status.

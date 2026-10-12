---
name: gif
description: Create DesignHub GIF candidates through the installed sprite-gen component-row pipeline, motion QA and GIF metadata.
---

# GIF with sprite-gen

[Korean](SKILL.ko.md)

Read the installed sprite-gen SKILL.md and resolve its actual path. Consult its current versioned docs before use. Do not copy the engine or assume a developer's home path.

Follow sprite-gen's user-workflow guide with choices already stated by the user. For this Codex workflow, select GPT rows and pass `--provider codex` explicitly. Use Grok video only when that route is requested; never switch to billed API generation automatically or save defaults without consent.

1. Inspect and lock a complete base. Prepare a new run with short readable states. For smooth glass illustration, disable pixel-unfake.
2. Use sprite-gen's venv and request-generated prompts: prepare → gen-set --provider codex → extract → compose-atlas → compose-gif → inspect. The component-row path uses chroma-key sources and omits --transparent; native PNG support does not change that contract. Take concurrency from the installed CLI.
3. Generate through Codex with the request's frame count, references, spacing and subject-safe key. Never substitute duplicated stills or locally drawn motion.
4. Preserve raw rows, frames, atlas, runtime manifest, GIF and QA reports. Compose through run-dir so curation is honored.
5. Inspect every frame and actual playback: motion, identity, scale, clipping, loop seam and ghosting. Regenerate a failing row.
6. Crop the final GIF to the union of visible pixels across all frames so no edge keeps a transparent margin: `python3 scripts/designhub_preflight.py crop <in.gif> <out.gif>` from this plugin's root. It keeps frame count, durations and loop. Then `python3 scripts/designhub_preflight.py margin <out.gif>` must print PASS: margin (0,0,0,0) and a short side of at least 700 px. If the crop leaves a short side under 700 px, regenerate larger; never upscale the crop (help center: 「최소 사이즈 규격 미달인 png는 별도로 크기를 늘려 등록하지 않습니다」). DesignHub rejected three GIFs on 2026-10-11 for uncropped margins ([records](../../records/designhub-rejected-elements.csv)).
7. Deliver verified files first. Curation is optional: open the Korean view when requested or already selected, then provide its URL.

When using sprite-gen gen for a separate transparent still or reference edit, pass `--provider codex --transparent --alpha-mode native`. Its auto strategy can choose chroma when references are attached; preserve glass alpha by selecting native explicitly. This still-image setting does not apply to animation rows.

GIF has palette-limited color and binary transparency; it cannot preserve PNG's continuous partial alpha. Keep RGBA sources and report glass-translucency loss. The image model generates still frames, not a native animated GIF.

Check hardware encoding support first. If there is no hardware GIF palette/LZW encoder, use sprite-gen's CPU writer and state why.

Before submitting a GIF whose only motion is a simple sway, twinkle or bob (살랑·반짝·통통), ask the user. The help center [GIF 애니](https://miricanvas-designhub.zendesk.com/hc/ko/articles/20537903229721) lists 「단순한 배치의 변화만 적용된 경우」 and 「미리캔버스 사용자가 제작할 수 있는 단순한 움직임의 GIF」 as rejection reasons. Never resubmit a GIF rejected for quality: 「품질 문제로 거부된 콘텐츠는 다시 제출할 수 없으며 해당 콘텐츠를 반복적으로 제출한 경우, 디자인허브 이용이 제한됩니다.」

Verify real animated GIF, multiple distinct frames, intended looping, a passing margin check after cropping, 700–1920 px per side, under 25 MB, and actual motion playback. Confirm current official DesignHub acceptance rules before submission.

CSV: extensionless fileName, contentType GIF, default tier Premium, 20–25 unique buyer-facing keywords, and no invented uniqueId. Follow [shared rules](../../SKILL.md) and [upload-csv](../upload-csv/SKILL.md). Report candidate quality separately from upload/review status.

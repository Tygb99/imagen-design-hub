---
name: png-element
description: MiriCanvas 또는 DesignHub PNG 요소 작업에 사용한다. imagegen source art, chroma-key 배경 제거, 투명 PNG 컷아웃, Photopea 마무리, 업로드 안전 PNG basename, PNG element CSV 행을 다룬다.
metadata:
  short-description: image-gen, chroma cleanup, Photopea, fringe QA를 포함한 DesignHub PNG 요소 경로
---

# Imagen Design Hub: PNG 요소

[English version](SKILL.md)

사용자가 `png요소`, 투명 PNG, cutout, sticker, element, 배경 제거, Photopea, 업로드용 alpha asset, magenta/purple fringe cleanup을 말할 때 이 경로를 사용한다.

이 스킬은 의도적으로 compact하게 유지한다. 전체 PNG 요소 workflow는 `references/full-workflow.ko.md`에 있고, 영어 원문은 `references/full-workflow.md`에 있다. 현재 단계에 필요한 section만 읽고 그대로 실행한다.

공유 route map이 필요하면 `../../SKILL.ko.md`를 읽어 PNG, JPG, SVG, GIF, upload CSV 전체 라우팅을 확인한다.

## 필수 첫 단계

1. `references/full-workflow.ko.md`를 연다.
2. source 생성, 배경 제거, PNG batch ready 판단 전에 **Route Triggers**, **Core Rules**, **Chroma-Key Workflow**, **Magenta Fringe Decontamination**, **Output Contract**, **Validation**을 읽는다.
3. plugin-wide routing, CSV upload, SVG/GIF route, shared metadata rule을 만지면 `../../SKILL.ko.md`도 읽는다.

## 불변 규칙

- source 생성에는 설치된 `$image-gen` 스킬을 사용해 새 `codex exec` 세션에서 생성한다. 내부 이미지 도구는 built-in `image_gen`이다.
- source 파일은 `assets/source-imagegen/`에 보존한다. 원본 생성 결과를 덮어쓰지 않는다.
- 완전히 평평한 단색 chroma-key 배경으로 생성한다. imagegen에 투명 배경이나 체크보드 배경을 요청하지 않는다.
- 먼저 `../../scripts/chroma_key.py`를 실행해 `assets/raw/`로 출력한다. DesignHub PNG 요소 작업에는 `.system/imagegen/remove_chroma_key.py`를 사용하지 않는다.
- magenta-fringe decontamination은 key가 magenta/purple이고 프롬프트가 피사체 내부의 pink, purple, magenta 사용을 금지한 경우에만 사용한다.
- 업로드용 DesignHub PNG는 Photopea 또는 프로젝트 Photopea runner를 거쳐 `assets/processed/`로 마무리한다.
- contact sheet는 preview artifact일 뿐이다. 최종 업로드 PNG를 contact sheet에서 잘라 만들지 않는다.
- 사용자가 명시적으로 확인하지 않았다면 외부 DesignHub 업로드/제출은 수행하지 않는다.

## 폴더 구조

이 스킬은 compact한 `ulw-loop` 스타일 layout을 따른다.

- `SKILL.md`: compact entrypoint, trigger, first steps, non-negotiables
- `SKILL.ko.md`: 한국어 companion entrypoint
- `references/full-workflow.md`: 전체 영어 workflow
- `references/full-workflow.ko.md`: 전체 한국어 workflow
- `agents/openai.yaml`: app/plugin-facing prompt metadata

## Codex 도구 매핑

| Workflow intent | Codex surface |
| --- | --- |
| Source generation | built-in `image_gen` 기반 `$image-gen` 스킬 |
| Alpha extraction | `../../scripts/chroma_key.py` |
| Upload-ready PNG finishing | Photopea 또는 project Photopea runner |
| Visual QA | checkerboard, white, dark preview |
| Metadata | `contentType` 값이 `PNG element`인 DesignHub CSV |

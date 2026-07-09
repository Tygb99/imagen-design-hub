---
name: aside-chatgpt-transparent
description: Aside로 ChatGPT native transparent 이미지 출력을 제어해 MiriCanvas/DesignHub 투명 PNG 배치를 만들 때 사용한다. 1장씩 프롬프트, 2분 대기, 다운로드 확보, 로컬 alpha/background 검수, Photopea 후처리, 350 DPI 리사이즈, metadata CSV, 구매자 검색 키워드 정리를 다룬다. 사용자가 Aside, ChatGPT, GPT Images native transparent, 직접 투명 PNG 생성, 로컬 검수, Photopea 후처리, DesignHub PNG 요소 키워드 생성을 말하면 이 스킬을 사용한다.
metadata:
  short-description: Aside + ChatGPT native transparent PNG 생성, 검수, Photopea, 키워드 경로
---

# Imagen Design Hub: Aside ChatGPT Transparent

[English version](SKILL.md)

사용자가 ChatGPT/Aside로 native transparent PNG 요소를 만들고, 이후 로컬 검수, Photopea 마무리, DesignHub용 메타데이터까지 기대할 때 이 경로를 사용한다. 이 경로는 chroma-key `png-element`와 다르다. source가 이미 RGBA/native transparent이므로 위험 지점은 key-color 제거가 아니라 alpha 품질, 숨은 투명 구멍, 낮은 해상도, 잘린 피사체다.

## 먼저 읽기

1. Aside로 ChatGPT를 조작해야 하면 설치된 `aside-browser` 스킬을 읽는다.
2. 공유 PNG 출력 규칙은 `../../skills/png-element/SKILL.ko.md`를 읽는다.
3. 키워드를 쓰기 전에 `../../references/keyword-generation.ko.md`를 읽는다.
4. upload CSV, SVG/GIF, JPG 배경, 공통 route 선택이 섞이면 `../../SKILL.ko.md`를 읽는다.

## 언제 쓰나

이 경로는 다음 상황에 사용한다.

- 사용자가 `aside`, `ChatGPT`, `native transparent`, GPT Images 투명 PNG, 직접 투명 출력을 요청한다.
- 피사체에 복잡한 edge, 유리, 머리카락, 천, 깃발, 구멍, key color와 충돌할 색이 있어 chroma-key 제거가 부적절하다.
- native 1024px 출력 이후에도 DesignHub/MiriCanvas PNG 요소 마무리, 350 DPI, tight crop, CSV metadata가 필요하다.
- 업로드 전에 다운로드 결과를 로컬에서 검사하라고 요청한다.

JPG 배경, SVG, GIF, 업로드 후 CSV 왕복에는 이 경로를 쓰지 않는다. 각각 맞는 플러그인 스킬로 보낸다.

## 경계

- 사용자가 외부 작업을 명시적으로 요청하지 않았다면 DesignHub 업로드, CSV 업로드, 최종 제출을 하지 않는다.
- ChatGPT native transparency를 자동으로 깨끗하다고 믿지 않는다. 흰 영역, 기호 사이, anti-aliased 디테일 아래에 투명 픽셀이 숨어 있을 수 있다.
- 원본 다운로드를 덮어쓰지 않는다. 먼저 보존한 뒤 processed output을 만든다.
- contact sheet에서 최종 업로드 PNG를 잘라 만들지 않는다.
- ChatGPT가 반복해서 생성 실패를 표시하거나 약속한 대기 시간 이후에도 멈춰 있으면, 보이는 상태를 기록하고 멈추거나 계속할지 확인한다.

## 권장 폴더

```text
outputs/<run-id>/
  assets/source-aside-chatgpt/
  assets/processed-aside-chatgpt/
  assets/replaced-or-repaired/<timestamp>/
  metadata/aside-chatgpt-preupload.csv
  review/aside-chatgpt/
  logs/aside-chatgpt-generation.json
```

현재 프로젝트에 이미 다른 폴더 관례가 있으면 그 관례를 따르고, 최종 보고에서 매핑을 설명한다.

## Aside 생성 워크플로

1. ChatGPT를 열기 전에 batch 주제, 개수, 사실 기반 시각 규칙을 확정한다.
2. 로그인된 ChatGPT 생성은 `aside exec`를 사용한다. 정확한 screenshot, snapshot, download evidence가 필요하면 `aside repl`을 사용한다.
3. 사용자가 비교 후보를 요청하지 않았다면 이미지는 1장씩 만든다.
4. 사용자가 2분 대기 규칙을 줬다면 각 prompt 뒤 약 2분까지 완료를 기다린다. 이미지가 나오지 않으면 정확한 표시 상태를 기록한다.
5. 이미지는 먼저 Aside session artifacts로 다운로드하고, 이후 `assets/source-aside-chatgpt/`로 복사한다.
6. 다음 이미지로 넘어가기 전에 다운로드를 로컬에서 확인한다.
   - 파일이 있고 byte size가 0보다 큼
   - PNG signature가 유효함
   - mode가 RGBA이거나 alpha channel이 있음
   - transparent pixel이 있음
   - UI screenshot, error panel, checkerboard, watermark, 중복 실패 후보가 아님
7. prompt, source path, size, alpha extrema, hash, ChatGPT 표시 상태를 manifest에 남긴다.

## 프롬프트 형태

간결하게 쓰고 금지 조건을 명확히 한다.

```text
Create one native transparent PNG element for MiriCanvas/DesignHub.
Subject: <single subject>
Style: <style>
Composition: fully visible subject, centered, no cropping, no extra background scene
Transparency: native transparent background, no checkerboard, no solid background, no drop shadow unless requested
Quality constraints: no text, no watermark, no logo, no UI frame, no signature
Factual constraints: <flags, symbols, counts, positions, required references>
```

국기, 배지, 숫자, 역사 사물처럼 사실 기반 기호가 있으면 이미지를 통과시키기 전에 신뢰할 수 있는 기준으로 시각 규칙을 확인한다. 사용자가 엄격한 로컬 기준 파일을 제공했다면 그 파일을 우선한다.

## 로컬 검수

checkerboard, white, dark 배경 검수 sheet를 만든다. 전체 보기와 확대 보기를 모두 확인한다.

확인할 것:

- 피사체가 전부 보이고 잘리지 않았다.
- alpha bbox가 현재 프로젝트 기준에 맞게 충분히 tight하다.
- 사각형 배경 잔여물이 없다.
- 흰색 또는 밝은 피사체 영역에 어두운 배경에서만 보이는 숨은 투명 구멍이 없다.
- 세부 디테일이 실수로 투명/반투명해지지 않았다.
- 중요한 사실 기반 디테일이 맞고 셀 수 있다.
- 여러 다운로드가 사용자가 의도한 경우가 아니라면 중복이 아니다.

숨은 투명도 검사는 이미지 border와 연결되지 않은 transparent 또는 very-low-alpha component를 찾는다. 큰 내부 component가 있으면 수동 검수 대상으로 표시한다. 흰 깃발, 종이, 의복, 표지판은 특히 어두운 배경 preview에서 확인한다.

## Photopea 마무리

ChatGPT native transparent 출력은 보통 1024px와 낮은 DPI다. source로 취급하고 final로 보지 않는다.

1. source 다운로드는 `assets/source-aside-chatgpt/`에 보존한다.
2. 프로젝트 Photopea runner가 있으면 먼저 실행한다. `miricanvas-design`에서는 다음을 우선한다.
   ```bash
   node src/cli.mjs photopea-runner --run outputs/<run-id>
   ```
3. 프로젝트 runner가 없으면 `../../scripts/write_photopea_runner.py`의 번들 runner 패턴을 사용한다.
4. 사용자가 달리 말하지 않았다면 최종 PNG는 로컬 DesignHub 관례를 만족해야 한다.
   - alpha가 있는 PNG
   - 짧은 변 최소 2500px
   - 350 DPI
   - tight crop, 보통 margin 0에서 3px 미만
5. Photopea 이후에도 다시 검증한다. resize/trim 과정에서 저알파 구멍이나 edge artifact가 드러날 수 있다.

## 메타데이터와 키워드

processed filename이 확정된 뒤 CSV 행을 만든다.

기본 header:

```text
fileName,uniqueId,elementName,keywords,tier,contentType
```

규칙:

- `fileName`: processed PNG와 맞는 basename. 로컬 CSV 계약이 확장자 제거를 요구하면 확장자 없이 쓴다.
- `uniqueId`: DesignHub 파일 업로드 전에는 빈칸.
- `tier`: 사용자가 달리 말하지 않으면 `Premium`.
- `contentType`: `PNG element`.
- `keywords`: 20~25개의 고유한 구매자 검색어.
- `ChatGPT`, `Aside`, `Photopea`, `imagegen`, `native transparent`, `PNG`, `DPI`, `CSV`, `DesignHub`, `MiriCanvas`, `Premium`, 날짜, run ID, 업로드 라벨 같은 제작/파일/관리 용어를 제거한다.
- `3.1절`, `광복절`, 현재 챌린지 주제처럼 사용자가 요구한 이벤트/주제어가 의미상 맞으면 유지한다.

## 수리와 교체 판단

- 구조적으로 틀렸거나, 심하게 잘렸거나, 사실 기준이 틀렸으면 수리보다 교체한다.
- 문제없이 좋은 이미지에 국소 alpha 결함만 있으면 원본을 보존하고 copy를 수리한다. before/after hash와 review sheet가 있는 repair manifest를 남긴다.
- 사실 기준이 엄격하면 생성된 피사체를 많이 덧칠하는 것보다 명확한 교체를 우선한다.

## 최종 보고

다음을 보고한다.

- Aside/ChatGPT surface와 1장씩 생성 여부
- source folder와 processed folder
- metadata CSV path와 keyword count
- checkerboard, white, dark review sheet
- Photopea 사용 여부와 최종 PNG 규격
- 교체, 수리, 거절한 다운로드
- 외부 업로드, CSV 업로드, 최종 제출 여부. 하지 않았다면 하지 않았다고 말한다.

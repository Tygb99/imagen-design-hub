---
name: imagen-design-hub
description: DesignHub 네이티브 투명 PNG 추천·제작, JPG 배경, SVG 요소, sprite-gen GIF, 업로드 CSV, 승인 요소 컬렉션을 처리합니다.
---

# Imagen Design Hub 0.7.0

[English](SKILL.md)

무엇을 만들지 물으면 PNG 요소를 기본으로 추천한다. 주제·스타일·사용처·구매자 검색어를 담은 구체적 콘셉트 3~5개를 제시한다.

## 경로

- 투명 PNG: [png-element](skills/png-element/SKILL.ko.md). 내장 image_gen에 실제 투명 배경을 요청하고 원본 알파를 보존한다.
- JPG 배경: [jpg-background](skills/jpg-background/SKILL.ko.md). 피사체 없는 그래픽 또는 특정 피사체가 돋보이지 않는 조화로운 패턴, 원본 PNG 보존, RGB JPG, Background CSV. 실사·실사풍 이미지는 Photo로 구분한다.
- SVG: [svg-beta](skills/svg-beta/SKILL.md). 실제 벡터 요소.
- GIF: [gif](skills/gif/SKILL.ko.md). 설치된 sprite-gen의 component-row 파이프라인과 실제 재생 검수.
- 업로드: [upload-csv](skills/upload-csv/SKILL.ko.md). Aside의 파일 직접 지정을 우선하고 실패하면 파일 선택 창을 사용한다. CSV 병합은 로컬 도구.
- 컬렉션: [collection](skills/collection/SKILL.ko.md). 현재 한도와 기존 소속 확인, 승인·공개 요소 묶기, 제목·키워드 등록·수정, 저장된 ID와 구성 확인.

## 네이티브 투명 배경

생성 전에 지연 로딩 도구를 포함해 이 세션에 실제 제공된 도구를 확인한다. `image_gen`은 네임스페이스 또는 `image_gen__imagegen`처럼 표시될 수 있으므로 문자 그대로의 함수명 일치만으로 없다고 판단하지 말고 실제 제공된 이름으로 호출한다. 플러그인 설치가 호스트 도구를 추가하지는 않는다. Codex Free 플랜의 ChatGPT 로그인에는 이미지 생성이 포함되지 않으며 지원되는 ChatGPT 세션의 내장 경로에는 API 키가 필요 없다. 도구가 없다는 이유로 플랜을 단정하지 않는다.

내장 도구가 없으면 생성을 멈추고 [이미지 생성 진단](references/image-generation-troubleshooting.ko.md)에 따라 CLI 설치·경로, CLI 버전, 로그인 방식·플랜, 기능 플래그, 제공자·모델을 구분한다. 관찰한 값과 추가 확인이 필요한 항목을 나누어 보고한다. Windows나 `codex exec`를 일괄 미지원으로 단정하지 않는다. API 키 CLI나 브라우저로 자동 전환하지 말고 사용자가 명시적으로 선택한 범위에서만 대안을 쓴다.

[Images 2.5 공식 발표](https://openai.com/index/introducing-chatgpt-images-2-5/)에서 Codex와 투명 배경 지원을 확인했다. 네이티브 투명을 먼저 요청한다. 반환 증거 없이 세부 모델을 Flare/Sunburst라고 단정하지 않는다.

요소 하나당 원본 하나를 생성하고 assets/source-imagegen/에 보존한다. 후처리본은 분리한다. 유리·안개·머리카락·발광의 의도된 부분 알파를 보존한다.

브라우저 생성은 명시적 요청에만 사용한다. 현재 ChatGPT 로그인에서 내장 도구가 제공되는 경우 네이티브 PNG에는 Aside·추가 로그인·API 키가 필요하지 않다.

트림·크기·DPI는 Pillow 또는 프로젝트 처리기로 맞춘다. 번들 고유 파일명 도구는 유지한다. `scripts/designhub_preflight.py`는 PNG·GIF를 그림 경계로 자르고, 올리기 전 투명 여백이 남은 파일을 실패시키며, `records/designhub-rejected-elements.csv`에 있는 이름을 멈춘다. sprite-gen 행 생성의 크로마 추출은 GIF 전용이며 PNG에 적용하지 않는다. 설치된 스킬을 읽고 엔진을 플러그인에 복제하지 않는다.

## 산출물·메타데이터

프로젝트 기준을 우선한다. 로컬 PNG 관례: 양변 최소 2500px·최대 9000px, 350 DPI, 50MB 미만, 잘림 없는 타이트한 경계. GIF 후보: 양변 700~1920px, 25MB 미만. 제출 전 현재 공식 접수 기준을 확인한다.

CSV 헤더는 fileName,uniqueId,elementName,keywords,tier,contentType이다. [키워드 지침](references/keyword-generation.ko.md)에 따라 중복 없는 구매자 검색어 20~25개를 쓰고 도구명·제작과정·파일형식·관리용어·실행 ID·날짜는 제외한다. 요청 없이는 언어를 섞지 않는다.

contentType은 PNG element, GIF, SVG element, Background, Photo, Photo(Cut-out) 중 맞는 값을 쓰고 tier 기본은 Premium이다. 업로드 전 uniqueId는 비운다. 업로드 후 DesignHub CSV를 내려받아 모든 행·ID를 보존하며 병합·재업로드하고 처리 행 수를 확인한다. 파일명은 실제 파일·다운로드 CSV에 맞춘다. scripts/prepare_designhub_unique_upload.py로 별도 고유 파일명 복사본을 만들 수 있다.

같은 파일·목적지의 승인은 재요청하지 않는다. 무관한 선택 항목을 변경하지 않고 파일 업로드·메타데이터 등록·심사 상태를 구분해 보고한다.

## 검증

시그니처·크기·DPI·피사체 경계·용량·CSV 대응을 검사한다. GIF는 실제 재생으로 움직임을 확인한다. 원본과 실패 후보를 보존하며 경로·생성 출처·측정값·품질 한계·외부 작업 여부를 보고한다.

## 플러그인 업데이트

현재 작업 방식과 맞지 않는 지침은 교체하거나 삭제한다. 경로별 스킬·번역·README·manifest 프롬프트·소개 페이지·참고 문서·평가 기준을 함께 맞추고, 새 규칙을 추가하면서 폐기된 규칙을 남기지 않는다. 리소스를 삭제하기 전에는 사용처를 확인한다. 실행은 현재 진입 문서와 경로별 스킬을 따르며, 과거 기록은 증거이지 현재 지침이 아니다.

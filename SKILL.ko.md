---
name: imagen-design-hub
description: DesignHub 네이티브 투명 PNG 추천·제작, JPG 배경, SVG 요소, sprite-gen GIF, 업로드 CSV를 처리합니다.
---

# Imagen Design Hub 0.5.0

[English](SKILL.md)

무엇을 만들지 물으면 PNG 요소를 기본으로 추천한다. 주제·스타일·사용처·구매자 검색어를 담은 구체적 콘셉트 3~5개를 제시한다.

## 경로

- 투명 PNG: [png-element](skills/png-element/SKILL.ko.md). 내장 image_gen에 실제 투명 배경을 요청하고 원본 알파를 보존한다.
- JPG 배경: [jpg-background](skills/jpg-background/SKILL.md). 화면을 채우는 배경, RGB JPG, Background CSV.
- SVG: [svg-beta](skills/svg-beta/SKILL.md). 실제 벡터 요소.
- GIF: [gif-beta](skills/gif-beta/SKILL.ko.md). 설치된 sprite-gen의 component-row 파이프라인과 실제 재생 검수.
- 업로드: [upload-csv](skills/upload-csv/SKILL.ko.md). 실시간 DesignHub 조작은 Computer Use, CSV 병합은 로컬 도구.

## 네이티브 투명 배경

[Images 2.5 공식 발표](https://openai.com/index/introducing-chatgpt-images-2-5/)에서 Codex와 투명 배경 지원을 확인했다. 네이티브 투명을 먼저 요청한다. 반환 증거 없이 세부 모델을 Flare/Sunburst라고 단정하지 않는다.

요소 하나당 원본 하나를 생성하고 assets/source-imagegen/에 보존한다. 후처리본은 분리한다. RGBA 모드뿐 아니라 완전 투명 외부 픽셀과 체크보드·흰색·어두운 배경을 확인한다. 유리·안개·머리카락·발광의 의도된 부분 알파를 보존한다. 보라색/초록색 전체나 낮은 알파를 일괄 제거하지 않는다.

크로마키 강제, 일괄 색 번짐 제거 레시피, 별도 Aside 투명 생성 경로는 폐기한다. 브라우저 생성은 명시적 요청에만 사용한다. 네이티브 PNG에는 Aside·추가 로그인·API 키가 필요하지 않다.

트림·크기·DPI는 Pillow 또는 프로젝트 처리기로 맞춘다. 필요한 수동 편집이나 명시적 요청에만 Photopea를 쓴다. 번들 Photopea·고유 파일명 도구는 유지한다. sprite-gen 행 생성의 크로마 추출은 GIF 전용이며 PNG에 적용하지 않는다. 설치된 스킬을 읽고 엔진을 플러그인에 복제하지 않는다.

## 산출물·메타데이터

프로젝트 기준을 우선한다. 로컬 PNG 관례: 양변 최소 2500px·최대 9000px, 350 DPI, 50MB 미만, 잘림 없는 타이트한 경계. GIF 후보: 양변 700~1920px, 25MB 미만. 제출 전 현재 공식 접수 기준을 확인한다.

CSV 헤더는 fileName,uniqueId,elementName,keywords,tier,contentType이다. [키워드 지침](references/keyword-generation.ko.md)에 따라 중복 없는 구매자 검색어 20~25개를 쓰고 도구명·제작과정·파일형식·관리용어·실행 ID·날짜는 제외한다. 요청 없이는 언어를 섞지 않는다.

contentType은 PNG element, GIF, SVG element, Background, Photo, Photo(Cut-out) 중 맞는 값을 쓰고 tier 기본은 Premium이다. 업로드 전 uniqueId는 비운다. 업로드 후 DesignHub CSV를 내려받아 모든 행·ID를 보존하며 병합·재업로드하고 처리 행 수를 확인한다. 파일명은 실제 파일·다운로드 CSV에 맞춘다. scripts/prepare_designhub_unique_upload.py로 별도 고유 파일명 복사본을 만들 수 있다.

같은 파일·목적지의 승인은 재요청하지 않는다. 무관한 선택 항목을 변경하지 않고 파일 업로드·메타데이터 등록·심사 상태를 구분해 보고한다.

## 검증

시그니처·크기·DPI·알파 분포·피사체 경계·용량·CSV 대응을 검사한다. PNG와 GIF 프레임을 체크보드·흰색·어두운 배경에서 확인하고 GIF는 실제 재생한다. 원본과 실패 후보를 보존하며 경로·생성 출처·측정값·품질 한계·외부 작업 여부를 보고한다.

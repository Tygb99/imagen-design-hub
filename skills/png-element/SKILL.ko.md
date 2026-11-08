---
name: png-element
description: PNG 요소를 추천하고 image_gen 네이티브 투명 출력, 알파 보존 후처리, 검수, 메타데이터로 제작합니다.
---

# PNG 요소

[English](SKILL.md)

[공통 규칙](../../SKILL.ko.md)을 읽는다. 추천에는 주제·스타일·사용처·구매자 검색어를 담은 콘셉트 3~5개를 제시한다.

공통 규칙의 Images 2.6 기준을 따르며 실제 내장 도구가 노출한 옵션만 사용한다. 참조 편집·시리즈는 대상을 먼저 확인하고 검수한 기준 이미지를 지원되는 방식으로 입력한다. 변경할 부분을 지정하고 정체성·형태·팔레트·부분 알파를 유지한다. 원본과 수정본은 각각 보존한다. API의 quality·complexity·markup은 사용자가 API 경로를 명시적으로 선택했을 때 사용하는 옵션이며 [상세 안내](../../references/2026-11-06-22-36-21-images-2-6.ko.md)를 따른다.

1. 공통 규칙에 따라 내장 이미지 도구 제공 여부부터 확인하고 설치된 imagegen 스킬에 따라 실제 투명 배경을 명시해 요소 하나당 한 번 생성한다. 내장 도구가 없으면 멈추고 [이미지 생성 진단](../../references/image-generation-troubleshooting.ko.md)을 따른다. 곧바로 API 키 대안으로 넘어가거나 계정이 Free라고 단정하지 않는다.
2. 원본은 assets/source-imagegen/에 보존한다. 자식 세션·브라우저·API 키·크로마키·배경 제거를 필수화하지 않는다.
3. Pillow 또는 프로젝트 처리기로 별도 복사본의 크기·DPI·용량을 맞춘다. 트림은 플러그인 루트에서 `python3 scripts/designhub_preflight.py crop <입력.png> <출력.png>`로 하며 DPI는 유지된다.
4. 고유 파일명과 구매자 검색어 20~25개의 PNG element CSV를 만든다. 승인된 업로드는 [upload-csv](../upload-csv/SKILL.ko.md)를 따른다.
5. 올리기 직전에 `python3 scripts/designhub_preflight.py margin <최종.png> ...`를 실행한다. 상하좌우 여백 (0,0,0,0)과 짧은 변 700px 이상인 PASS 파일만 올린다. FAIL은 0이 아닌 종료 코드를 내며 그 파일은 올리지 않는다. 2026-10-11 PNG 요소 6개가 이 경로에 트림이 있었는데도 여백 때문에 거부됐다([기록](../../records/designhub-rejected-elements.csv)).

두 명령 모두 알파 8/255(약 3%) 이하를 빈 캔버스로 본다. 이 정도로 옅은 그림자·빛 번짐 픽셀은 화면에서 안 보이지만 단순 `getbbox()` 트림 범위를 넓혀 눈에 보이는 여백을 남긴다. crop과 margin에 같은 문턱값을 쓰고, 바꿀 때는 사용자 승인을 받는다.

유리·반투명 효과의 부분 알파를 보존하며 GIF 크로마 제거를 적용하지 않는다. 네이티브 출력이 반복 실패하면 알리고 요청 범위에서 대안을 선택한다.

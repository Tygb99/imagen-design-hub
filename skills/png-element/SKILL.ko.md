---
name: png-element
description: PNG 요소를 추천하고 image_gen 네이티브 투명 출력, 알파 보존 후처리, 검수, 메타데이터로 제작합니다.
---

# PNG 요소

[English](SKILL.md)

[공통 규칙](../../SKILL.ko.md)을 읽는다. 추천에는 주제·스타일·사용처·구매자 검색어를 담은 콘셉트 3~5개를 제시한다.

1. 설치된 imagegen 스킬에 따라 내장 image_gen으로 실제 투명 배경을 명시하고 요소 하나당 한 번 생성한다.
2. 원본은 assets/source-imagegen/에 보존한다. 자식 세션·브라우저·API 키·크로마키·배경 제거를 필수화하지 않는다.
3. Pillow 또는 프로젝트 처리기로 별도 복사본의 크기·DPI·용량을 맞춘다. 트림은 플러그인 루트에서 `python3 scripts/designhub_preflight.py crop <입력.png> <출력.png>`로 하며 DPI는 유지된다.
4. 고유 파일명과 구매자 검색어 20~25개의 PNG element CSV를 만든다. 승인된 업로드는 [upload-csv](../upload-csv/SKILL.ko.md)를 따른다.
5. 올리기 직전에 `python3 scripts/designhub_preflight.py margin <최종.png> ...`를 실행한다. 상하좌우 여백 (0,0,0,0)과 짧은 변 700px 이상인 PASS 파일만 올린다. FAIL은 0이 아닌 종료 코드를 내며 그 파일은 올리지 않는다. 2026-10-11 PNG 요소 6개가 이 경로에 트림이 있었는데도 여백 때문에 거부됐다([기록](../../records/designhub-rejected-elements.csv)).

두 명령 모두 알파 8/255(약 3%) 이하를 빈 캔버스로 본다. 이 정도로 옅은 그림자·빛 번짐 픽셀은 화면에서 안 보이지만 단순 `getbbox()` 트림 범위를 넓혀 눈에 보이는 여백을 남긴다. crop과 margin에 같은 문턱값을 쓰고, 바꿀 때는 사용자 승인을 받는다.

유리·반투명 효과의 부분 알파를 보존하며 GIF 크로마 제거를 적용하지 않는다. 네이티브 출력이 반복 실패하면 알리고 요청 범위에서 대안을 선택한다.

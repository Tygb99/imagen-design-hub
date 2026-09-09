---
name: gif-beta
description: 설치된 sprite-gen의 component-row 파이프라인, 모션 검수, GIF 메타데이터로 DesignHub 후보를 제작합니다.
---

# sprite-gen GIF

[English](SKILL.md)

설치된 sprite-gen의 SKILL.md와 실제 경로를 확인한다. 통합 기준은 2.0.3이다. 엔진 복제나 개발자 홈 경로 가정을 하지 않는다.

1. 전체가 보이는 베이스를 검수·고정하고 새 런에 짧은 동작을 선언한다. 부드러운 유리 일러스트는 pixel-unfake를 끈다.
2. 전용 venv와 요청서 프롬프트로 prepare → gen → extract → compose-atlas → preview → compose-gif를 따른다. 2.0.3 행 생성은 여전히 크로마키를 요구한다.
3. Codex로 프레임 수·참조·간격·피사체와 겹치지 않는 키를 지켜 생성한다. 정지 이미지 복제나 로컬 그림으로 동작을 대체하지 않는다.
4. 원본 행·프레임·아틀라스·매니페스트·GIF·보고서를 보존한다. run-dir로 합성해 큐레이션을 반영한다.
5. 모든 프레임과 실제 재생에서 동작·형태·크기·잘림·루프·잔상을 검사한다. 실패한 행은 재생성한다.
6. 무인 배치가 아니면 한국어 큐레이션 뷰를 열고 URL을 전달한다.

GIF는 제한된 팔레트와 이진 투명도여서 PNG의 연속 부분 알파를 보존하지 못한다. RGBA 원본을 남기고 유리의 반투명 손실을 알린다. 이미지 모델은 정지 프레임을 생성하며 네이티브 GIF 생성이 아니다.

하드웨어 인코딩을 먼저 확인하고 GIF 팔레트/LZW 하드웨어 인코더가 없으면 이유를 밝히고 sprite-gen CPU 인코더를 사용한다.

실제 애니메이션 GIF, 서로 다른 복수 프레임, 의도된 루프, 양변 700~1920px, 25MB 미만, 체크보드·흰색·어두운 배경 재생을 검증한다. 제출 전 현재 공식 DesignHub 기준을 확인한다.

CSV는 확장자 없는 fileName, contentType GIF, 기본 tier Premium, 중복 없는 검색어 20~25개를 쓴다. uniqueId는 임의 생성하지 않는다. [공통 규칙](../../SKILL.ko.md)과 [upload-csv](../upload-csv/SKILL.ko.md)를 따른다. 품질과 업로드·심사 상태를 구분해 보고한다.

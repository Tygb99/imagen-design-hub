---
name: svg-beta
description: DesignHub 실제 벡터 SVG 요소와 SVG element CSV를 제작합니다.
---

# SVG 요소 베타

[English](SKILL.md)

실제 벡터 원본으로 단순한 요소를 제작한다. 래스터 확장자 변경이나 주요 그림의 비트맵 삽입은 금지한다. 채움색과 테두리색을 합친 가시 색상은 5개 이하로 유지한다. 흰색·검정은 포함하고 투명·none은 제외한다. 불필요한 배경·아트보드·영역 밖 도형을 제거한다. 스크립트·외부 링크·foreignObject·숨은 워터마크·폰트 잔여물을 넣지 않는다.

업로드 전에 모든 가시 테두리를 채움색이 있는 윤곽선 경로로 변환한다. 모양과 색을 유지하고 `stroke="none"`을 포함한 모든 `stroke`·`stroke-*` 속성을 제거했는지 확인한다. 실제 DesignHub 업로더는 Stroke 속성이 있는 SVG를 거부한다. 오류를 피하려고 가시 테두리를 없애지 않는다.

올바른 XML과 타이트한 viewBox, 최대 6000px, 0.15MB 미만을 검증한다. CSV는 확장자 없는 fileName, contentType SVG element, 제공된 경우에만 uniqueId, 중복 없는 검색어 20~25개를 사용한다. 승인된 범위에서만 외부 업로드하며 베타 후보 품질과 실제 접수 상태를 구분한다.

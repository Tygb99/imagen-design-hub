# 2026-10-12에 확인한 디자인허브 거부 요소

[English](2026-10-12-designhub-rejections.md)

디자인허브 거부됨 목록에 단일 요소 12개가 있었다(2026-10-12 21:41~21:46 KST, 다시 제출하지 않고 읽기만 함). 기계가 읽는 목록은 [designhub-rejected-elements.csv](designhub-rejected-elements.csv)이고, `scripts/designhub_preflight.py rejected`가 업로드 전에 이 목록을 읽는다.

## 사유 코드

- **A** (GIF 3개): 크롭 안 된 투명 여백, 그리고 「품질 문제로 거부된 콘텐츠는 다시 제출할 수 없으며 해당 콘텐츠를 반복적으로 제출한 경우, 디자인허브 이용이 제한됩니다.」 다시 내지 않는다.
- **B** (PNG 요소 6개): 크롭 안 된 투명 여백. 대지를 피사체에 딱 맞춰 상하좌우 여백이 없어야 한다.
- **C** (배경 2개): 콘텐츠 타입 잘못. 피사체가 있는 일러스트는 배경이 아니라 요소 타입으로 낸다.
- **D** (PNG 요소 1개): 피사체 잘림 또는 배경 제거 불완전.

## 열

`no,elementName,fileName,contentType,submittedAt,rejectedAt,reasonCode`. 디자인허브 화면 값을 그대로 옮겼다(시각도 화면 표기). 새 거부는 같은 열로 행을 추가한다.

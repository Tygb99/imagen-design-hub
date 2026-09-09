# imagen-design-hub 0.5.0

[English](README.md)

PNG 요소를 추천하고 Codex로 네이티브 투명 소재를 생성한다. 로컬에서 크기·DPI를 맞추고 알파를 검수한 뒤 DesignHub 메타데이터를 준비한다.

## 경로

- PNG 추천·네이티브 투명: [png-element](skills/png-element/SKILL.ko.md)
- GIF 후보: [gif-beta](skills/gif-beta/SKILL.ko.md), 설치된 sprite-gen 2.0.3 사용
- 전체 배경: [jpg-background](skills/jpg-background/SKILL.md)
- 실제 벡터: [svg-beta](skills/svg-beta/SKILL.md)
- Computer Use 업로드·CSV: [upload-csv](skills/upload-csv/SKILL.ko.md)

## 0.5.0 변경

PNG 기본 경로를 내장 image_gen 네이티브 투명으로 바꿨다. 크로마키 강제·일괄 색 번짐 제거·별도 Aside 투명 스킬을 삭제했다. 부분 알파를 보존하고 체크보드·흰색·어두운 배경을 검수한다. Photopea는 선택 사항이며 수동 편집용 runner는 유지한다.

GIF는 sprite-gen의 component-row 생성·추출을 쓴다. 현재 행 생성 계약은 크로마키다. GIF의 이진 투명도와 제한된 팔레트 때문에 유리 반투명이 RGBA PNG와 같을 수 없다. 원본 프레임을 보존하고 실제 동작을 검수한다.

[Images 2.5 공식 발표](https://openai.com/index/introducing-chatgpt-images-2-5/)에 Codex·투명 배경 지원이 명시돼 있다. 도구 제공 여부로 세부 모델을 단정하지 않는다.

## 설치·업데이트

저장소를 복제하고 번들 설치기로 로컬 마켓플레이스에 등록한다.

```sh
git clone https://github.com/Tygb99/imagen-design-hub.git
cd imagen-design-hub
node scripts/register_marketplace.mjs
```

이미 등록된 플러그인은 원본을 업데이트한 뒤 자신의 마켓플레이스 이름으로 재설치한다. 이 컴퓨터에서는 다음 명령을 쓴다.

```sh
codex plugin add imagen-design-hub@tygb99-personal
```

새 작업에서 갱신된 스킬을 읽는다. npm 패키지 설치는 필요 없다. 기존 자동 업데이트는 깨끗한 원본 체크아웃만 fast-forward하며 로컬 편집을 보존한다. 로컬 수정·재설치는 공개 배포나 GitHub push가 아니다.

## 의존성

- PNG 생성: Codex 내장 image_gen, API 키 불필요
- 로컬 마무리: Python·Pillow
- GIF: 설치된 sprite-gen과 전용 venv, 해당 버전 SKILL.md
- DesignHub 실시간 조작: Computer Use
- 설치·갱신: Node 18+·Git
- 필요한 수동 편집 또는 명시적 요청: Photopea

[작업 규칙](SKILL.ko.md), [키워드 지침](references/keyword-generation.ko.md), [형식 가이드](references/designhub-element-guide-map.ko.md)를 읽는다. 원본과 파생본을 분리하고 업로드 파일명·다운로드 uniqueId 대응을 유지한다.

MIT: [LICENSE](LICENSE).

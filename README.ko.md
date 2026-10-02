# imagen-design-hub 0.6.1

[English](README.md)

PNG 요소를 추천하고 Codex로 네이티브 투명 소재를 생성한다. 로컬에서 크기·DPI를 맞추고 DesignHub 메타데이터를 준비한다.

## 경로

- PNG 추천·네이티브 투명: [png-element](skills/png-element/SKILL.ko.md)
- GIF 후보: [gif](skills/gif/SKILL.ko.md), 설치된 sprite-gen 버전 기준
- 그래픽 배경·조화로운 패턴: [jpg-background](skills/jpg-background/SKILL.ko.md), 공식 Background/Photo 타입 구분
- 실제 벡터: [svg-beta](skills/svg-beta/SKILL.md)
- Aside 업로드·CSV: [upload-csv](skills/upload-csv/SKILL.ko.md), `setInputFiles()` 우선·파일 선택 창 전환

## 0.6.1 변경

공식 [배경 가이드](https://slashpage.com/designhub-guide/ndvwx728377exm3z6jpg)에 맞춰 JPG 지침을 갱신했다. 피사체 없는 그래픽 또는 특정 피사체가 돋보이지 않는 조화로운 패턴을 Background로 준비한다. 실사·실사풍은 Photo로 구분하고 중심 피사체 일러스트는 요소로 분리한다. 완성 포스터를 Background로 제출하거나 확장자 변경으로 타입을 맞추지 않는다.

공식 파일 규격과 로컬 DPI 목표를 구분하고, 다운로드 CSV의 모든 행·ID를 보존하며, 생성형 AI 표시를 확인한다. 경로 안내·가이드 맵·소개 페이지·평가 사례에서 자연 질감·실사풍을 무조건 배경으로 취급하던 안내를 교체했다.

PNG 기본 경로는 내장 image_gen의 네이티브 투명 생성이다. 의도한 부분 알파와 원본을 보존하고 Pillow 또는 기존 로컬 처리기로 트림·크기·DPI를 맞춘다.

GIF는 sprite-gen의 component-row 생성·추출을 쓴다. 현재 행 생성 계약은 크로마키다. GIF의 이진 투명도와 제한된 팔레트 때문에 유리 반투명이 RGBA PNG와 같을 수 없다. 원본 프레임을 보존하고 실제 동작을 검수한다.

[Images 2.5 공식 발표](https://openai.com/index/introducing-chatgpt-images-2-5/)에 Codex·투명 배경 지원이 명시돼 있다. 도구 제공 여부로 세부 모델을 단정하지 않는다.

## 설치·업데이트

개인 마켓플레이스가 가리키는 경로에 저장소를 복제한 뒤 등록·설치한다.

```sh
git clone https://github.com/Tygb99/imagen-design-hub.git "$HOME/plugins/imagen-design-hub"
node "$HOME/plugins/imagen-design-hub/scripts/register_marketplace.mjs"
codex plugin list
codex plugin add imagen-design-hub@<목록에 표시된 마켓플레이스 이름>
```

`codex plugin list`에 로컬 마켓플레이스가 보이지 않으면 `codex plugin marketplace add "$HOME"`를 한 번 실행하고 목록을 다시 확인한다.

이미 등록된 플러그인은 원본을 업데이트한 뒤 자신의 마켓플레이스 이름으로 재설치한다. 이 컴퓨터에서는 다음 명령을 쓴다.

```sh
codex plugin add imagen-design-hub@tygb99-personal
```

목록의 버전이 0.6.1인지 확인하고 새 작업에서 갱신된 스킬을 읽는다. 제거할 때는 `codex plugin remove imagen-design-hub@<마켓플레이스 이름>` 실행 후 `node "$HOME/plugins/imagen-design-hub/scripts/unregister_marketplace.mjs"`를 실행한다. npm 패키지 설치는 필요 없다. 기존 자동 업데이트는 깨끗한 원본 체크아웃만 fast-forward하며 로컬 편집을 보존한다. 로컬 수정·재설치는 공개 배포나 GitHub push가 아니다.

## 의존성

- PNG 생성: Codex 내장 image_gen, API 키 불필요
- 로컬 마무리: Python·Pillow
- GIF: 설치된 sprite-gen과 전용 venv, 해당 버전 SKILL.md
- DesignHub 조작: Aside REPL, 필요한 파일 선택 창 전환은 Computer Use
- 설치·갱신: Node 18+·Git

[작업 규칙](SKILL.ko.md), [키워드 지침](references/keyword-generation.ko.md), [형식 가이드](references/designhub-element-guide-map.ko.md)를 읽는다. 원본과 파생본을 분리하고 업로드 파일명·다운로드 uniqueId 대응을 유지한다.

MIT: [LICENSE](LICENSE).

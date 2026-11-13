# imagen-design-hub 0.9.0

[English](README.md) · [변경 이력](2026-11-13-22-10-33-CHANGELOG.ko.md)

PNG 요소를 추천하고 Images 2.6 생성·편집 지침에 따라 Codex로 네이티브 투명 소재를 생성한다. 로컬에서 크기·DPI를 맞추고 DesignHub 메타데이터를 준비하며 승인·공개 요소를 컬렉션으로 묶는다.

## 경로

- PNG 추천·네이티브 투명: [png-element](skills/png-element/SKILL.ko.md)
- GIF 후보: [gif](skills/gif/SKILL.ko.md), 설치된 sprite-gen 버전 기준
- 그래픽 배경·조화로운 패턴: [jpg-background](skills/jpg-background/SKILL.ko.md), 공식 Background/Photo 타입 구분
- 실제 벡터: [svg](skills/svg/SKILL.ko.md)
- Aside 업로드·CSV: [upload-csv](skills/upload-csv/SKILL.ko.md), `setInputFiles()` 우선·파일 선택 창 전환
- 컬렉션: [collection](skills/collection/SKILL.ko.md), 현재 한도·기존 소속·요소 묶기·제목과 키워드·등록·저장 결과 확인

## 0.9.0 변경

로컬 벡터 제작 인수 테스트를 거쳐 `svg-beta`를 `svg`로 전환했다. `$imagen-design-hub:svg`로 사용한다. SVG 에이전트 설정을 추가하고 실제 벡터·색상·윤곽선·파일·메타데이터 검수는 유지한다. 별도 실사용 테스트에서는 내장 image_gen의 PNG를 4색 SVG로 변환해 파일 1개 업로드, CSV 101행 처리, AI 표시 저장, 해당 1개 심사 제출을 완료했다. 2026-11-13에 확인한 DesignHub 화면에서 같은 SVG의 승인과 Premium 라이선스·생성형 AI 표시 유지가 확인됐다. 사용자 선택에 따라 API 경로는 실행하지 않았고 도구가 정확한 백엔드 모델을 식별하지 않았다.

[SVG 검수 보고서](records/2026-11-06-22-47-15-svg-qualification.ko.md) · [내장 생성·DesignHub 승인 검증](records/2026-11-13-22-10-33-native-svg-live.ko.md)

## 0.8.0 변경

[Images 2.6](https://openai.com/index/introducing-images-2-6/) 기준으로 PNG·JPG 생성, 참조 편집, SVG 안내를 갱신했다. 편집 시 피사체 정체성과 알파를 보존하고 변형에는 검수한 기준 이미지를 재사용한다. [Images 2.6 옵션](references/2026-11-06-22-36-21-images-2-6.ko.md)은 선택적 API quality·complexity, 수정 위치 지정, SVG 내보내기를 설명한다. 실제 도구 명세를 먼저 확인하며 API 지원을 내장 Codex 도구 지원으로 가정하지 않는다. 플러그인이 API 클라이언트를 추가하지는 않는다. GIF는 sprite-gen을 유지하고 Free 미지원 진단과 DesignHub 제출 검수를 계속 적용한다.

## 0.7.0 변경

한국어·영어 `collection` 스킬을 추가했다. 승인·공개 요소를 타입과 주제별로 묶고, 현재 한도 안에서 크기를 균등하게 나누며, 식별자 보존·기존 소속 확인·재시도 중복 방지·저장 결과 기록을 처리한다. 컬렉션 기록은 요소 CSV와 분리하며, 요청한 이름·키워드 수정은 기존 컬렉션에서 수행한다.

사용 예: “$imagen-design-hub:collection으로 승인·공개된 요소를 컬렉션으로 묶고 한국어 제목과 키워드 25개를 등록해줘.”

## 0.6.2 변경

디자인허브 반려 12건을 반영해 `scripts/designhub_preflight.py`를 추가했다: GIF 전체 프레임 크롭과 700px 재확인, PNG·GIF 알파 기준 여백 0 검사(알파 8/255 이하는 빈칸), `records/designhub-rejected-elements.csv`에 있는 이름은 업로드 중단. 단순한 움직임만 있는 GIF는 내기 전에 사용자에게 묻는다.

## 0.6.1 변경

공식 [배경 가이드](https://slashpage.com/designhub-guide/ndvwx728377exm3z6jpg)에 맞춰 JPG 지침을 갱신했다. 피사체 없는 그래픽 또는 특정 피사체가 돋보이지 않는 조화로운 패턴을 Background로 준비한다. 실사·실사풍은 Photo로 구분하고 중심 피사체 일러스트는 요소로 분리한다. 완성 포스터를 Background로 제출하거나 확장자 변경으로 타입을 맞추지 않는다.

공식 파일 규격과 로컬 DPI 목표를 구분하고, 다운로드 CSV의 모든 행·ID를 보존하며, 생성형 AI 표시를 확인한다. 경로 안내·가이드 맵·소개 페이지·평가 사례에서 자연 질감·실사풍을 무조건 배경으로 취급하던 안내를 교체했다.

PNG 기본 경로는 내장 image_gen의 네이티브 투명 생성이다. 의도한 부분 알파와 원본을 보존하고 Pillow 또는 기존 로컬 처리기로 트림·크기·DPI를 맞춘다.

GIF는 sprite-gen의 component-row 생성·추출을 쓴다. 현재 행 생성 계약은 크로마키다. GIF의 이진 투명도와 제한된 팔레트 때문에 유리 반투명이 RGBA PNG와 같을 수 없다. 원본 프레임을 보존하고 실제 동작을 검수한다.

[Images 2.6 공식 발표](https://openai.com/index/introducing-images-2-6/)를 현재 생성·편집 기준으로 삼는다. 실제 모델 버전과 변형은 도구가 식별해 준 경우에만 기록한다.

## 설치·업데이트

아래 명령을 실행할 터미널에서 Codex CLI가 먼저 동작해야 한다. 데스크톱 앱이나 플러그인을 설치했다고 PATH의 `codex` 명령까지 생기지는 않는다. Windows에서는 `Get-Command codex -All`과 `codex --version`부터 확인한다. 설치·계정 조건·도구 미제공 시 조치는 [이미지 생성 진단](references/image-generation-troubleshooting.ko.md)을 따른다.

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

목록의 버전이 0.9.0인지 확인하고 새 작업에서 갱신된 스킬을 읽는다. 제거할 때는 `codex plugin remove imagen-design-hub@<마켓플레이스 이름>` 실행 후 `node "$HOME/plugins/imagen-design-hub/scripts/unregister_marketplace.mjs"`를 실행한다. npm 패키지 설치는 필요 없다. 기존 자동 업데이트는 깨끗한 원본 체크아웃만 fast-forward하며 로컬 편집을 보존한다. 로컬 수정·재설치는 공개 배포나 GitHub push가 아니다.

## 의존성

- PNG 생성: 사용 가능한 내장 이미지 도구와 지원되는 ChatGPT 로그인. 이 네이티브 경로에는 API 키가 필요 없지만 Codex Free 플랜은 이미지 생성을 지원하지 않는다. 플러그인 설치만으로 활성화되지 않으므로 [조건·진단](references/image-generation-troubleshooting.ko.md)을 확인한다.
- 로컬 마무리: Python·Pillow
- GIF: 설치된 sprite-gen과 전용 venv, 해당 버전 SKILL.md
- DesignHub 조작: Aside REPL, 필요한 파일 선택 창 전환은 Computer Use
- 설치·갱신: Node 18+·Git

[작업 규칙](SKILL.ko.md), [키워드 지침](references/keyword-generation.ko.md), [형식 가이드](references/designhub-element-guide-map.ko.md)를 읽는다. 원본과 파생본을 분리하고 업로드 파일명·다운로드 uniqueId 대응을 유지한다.

MIT: [LICENSE](LICENSE).

# AI 스킬 상품화 검수 보고서

## 대상과 계약

- 스킬: `imagen-design-hub` 플러그인과 하위 route skills
- 버전 또는 검수 시각: `0.4.3`, 2026-08-18 00:20:21 KST
- 배포 포함 파일: Git 추적 파일, 기존 `records/*.md`, `scripts/unregister_marketplace.mjs`를 포함한 운영 파일 53개. 이 보고서 자체는 검수 증거 문서이므로 반복 실행 bundle hash 비교에서 제외했다.
- 대표 요청: 사용자 제공 PNG를 `png-element` 경로의 번들 chroma-key helper로 처리하고, DesignHub 고유 basename PNG와 CSV를 생성한다.
- 기대 산출물: 원본 보존, alpha PNG, 고유 basename PNG, 20개 고유 키워드를 가진 CSV, 정상적인 marketplace 등록과 제거.
- 탐색 경계: 플러그인 루트 전체, 최대 깊이 6, 상대 경로와 파일 집합은 사전순. 심링크는 따르지 않는다.
- 허용 변동: 새 임시 HOME/작업 폴더 경로만 허용한다. 입력·분기·출력 구조·판정은 동일해야 한다.
- PASS 조건: 파일 참조와 의존성이 선언되어 있고, 설치·활성화·제거·재로드 안내가 재현되며, 독립 실행 2회가 같은 판단 계약을 만족한다.

## 정적 검사

### 파일 참조

| 참조 | 읽는 단계 | 생성 단계 | 배포 포함 | 판정 | 증거 |
|---|---:|---:|---|---|---|
| `SKILL.md` → `SKILL.ko.md`, `references/designhub-element-guide-map.md` | 라우팅 | 아니오 | 예 | PASS | Markdown local link 검사에서 모두 존재 |
| `skills/png-element/`의 full workflow와 `../../scripts/*` | PNG 처리 전 | alpha/unique output 생성 | 예 | PASS | route root 기준 경로 검사 통과 |
| `skills/upload-csv/SKILL.md` ↔ `.ko.md` | CSV live action 전 | CSV 산출물 | 예 | PASS | 양국어 운영 함정과 Computer Use 경계 확인 |
| `src/cli.mjs` | 프로젝트가 제공할 때만 | 프로젝트 산출물 | 아니오 | PASS | 번들 미포함 사실을 문서에 명시하고 bundled runner fallback 제공 |

### 의존성

| 의존성 | 포함/생성/사용자 제공 | 안내 위치 | 판정 | 증거 |
|---|---|---|---|---|
| Node.js 18+, Git | 사용자 제공 | `README.md`, 설치 스크립트 | PASS | 두 임시 HOME에서 Node 등록/해제 실행 |
| Python 3.10+, Pillow | 사용자 제공 | `README.md`, `requirements.txt` | PASS | 두 실행에서 bundled `chroma_key.py` 성공 |
| `$image-gen` | 사용자 제공 | `SKILL.md`와 manifest default prompt | PASS | 생성 단계 외부 의존성으로 명시 |
| Computer Use, Photopea, Aside/ChatGPT, SVG editor, GIF encoder | 사용자 제공·해당 route에서만 필요 | route skills | PASS | live/editor 의존성을 route별로 명시하고 CSV live action 금지 경계 확인 |
| `src/cli.mjs` | 선택적 프로젝트 제공 | `SKILL.md`, `aside-chatgpt-transparent/SKILL.md` | PASS | 플러그인 번들 의존성이 아님을 명시 |

### 설치와 활성화

| 항목 | 문서 위치 | 실제 확인 방법 | 판정 |
|---|---|---|---|
| 복사 위치 | `README.md` 설치 예시 | 새 HOME의 `plugins/imagen-design-hub`에 배포 파일만 복사 | PASS |
| 런타임·권한 | README dependencies | Node/Python 실행과 로컬 파일 쓰기 | PASS |
| 재시작·재로드 | README install section | Codex 재시작 또는 plugin picker 재열기 안내 추가 | PASS |
| 인식 확인 | README install section | `register_marketplace.mjs` 실행 후 manifest와 marketplace entry 확인 | PASS |
| 제거 방법 | README와 `scripts/unregister_marketplace.mjs` | entry 제거 후 재등록으로 idempotent 경로 확인 | PASS |

## 테스트 1: 콜드 스타트 인수

- 새 환경: `/var/folders/3y/9l22xcm96ml9dkcdm5cftdh80000gn/T/productization-rerun-one-97vnyarl`
- 복사한 파일: 운영 배포 파일 53개, `.git`과 원본 작업 상태 제외
- 실행 명령 또는 도구 호출: `register_marketplace.mjs` → `unregister_marketplace.mjs` → 재등록 → `chroma_key.py` → `prepare_designhub_unique_upload.py`
- 입력: `input/source.png` 사용자 제공 입력으로 취급, `preupload.csv` 1행, 20개 고유 키워드
- 관찰한 결과: marketplace 등록·해제·재등록 성공, `output/raw/source-alpha.png`, `output/unique/smoke-01.png`, `output/metadata/unique.csv` 생성. 원본 hash 보존, PNG RGBA와 DPI 존재, CSV BOM 없음.
- 잘못된 입력 실행 결과: 존재하지 않는 images directory를 넣었을 때 non-zero 종료, `Images directory not found` 출력, `bad.csv` 미생성.
- 판정: `PASS`

## 테스트 2: 반복 일관성

- 첫 실행과 분리된 새 환경: `/var/folders/3y/9l22xcm96ml9dkcdm5cftdh80000gn/T/productization-rerun-two-16uht0qp`
- 실행 명령 또는 도구 호출: 테스트 1과 동일한 독립 실행
- 입력: 테스트 1과 동일한 배포 파일과 동일한 입력 계약

| 비교 항목 | 실행 1 | 실행 2 | 허용 변동 | 판정 |
|---|---|---|---|---|
| 탐색 파일 집합 | 53개, bundle hash `385533ce5a7e63619d5621100b524008e7d78beb84b3d07ff9fe6dc362d1b787` | 동일 | 임시 경로만 | PASS |
| 처리 순서 | register → unregister → register → chroma → unique CSV → negative input | 동일 | 없음 | PASS |
| 선택 입력 | `input/source.png` | 동일 | 없음 | PASS |
| 실행 분기 | 정상 경로와 missing-images 오류 경로 | 동일 | 없음 | PASS |
| 산출물 구조 | alpha PNG, `smoke-01.png`, `unique.csv` | 동일 | 임시 부모 경로만 | PASS |
| 최종 판정 | PASS | PASS | 없음 | PASS |

- 판정: `PASS`

## 발견한 결함과 수정

| 심각도 | 결함 | 재현 증거 | 수정 | 재검증 증거 |
|---|---|---|---|---|
| 높음 | 플러그인에 없는 `src/cli.mjs`가 번들 명령처럼 읽힐 수 있음 | bundle 파일 집합에 `src/cli.mjs` 없음 | 현재 프로젝트가 제공할 때만 사용하도록 명시하고 bundled runner/validation fallback 안내 | 정적 경로 검사와 두 콜드 스타트 통과 |
| 중간 | marketplace 제거 방법이 문서와 스크립트에 없음 | 설치는 가능하지만 등록 해제 경로가 없음 | `scripts/unregister_marketplace.mjs` 추가, 양국어 README에 제거·재로드 절차 추가 | 두 실행에서 등록·해제·재등록 성공 |

## 최종 판정

`PASS`

판정 근거:

- [x] 두 테스트를 서로 다른 새 환경에서 실행했다.
- [x] 유령 파일이 없다.
- [x] 미선언 외부 의존성이 없다.
- [x] 설치·활성화·제거·재로드 절차를 재현했다.
- [x] 탐색 경계와 처리 순서가 명시됐다.
- [x] 반복 실행의 판단 계약이 일치했다.
- [x] 각 주장에 실제 실행 증거가 있다.

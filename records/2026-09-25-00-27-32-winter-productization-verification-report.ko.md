# AI 스킬 상품화 검수 보고서

## 대상과 계약

- 스킬: `imagen-design-hub` 0.5.1의 `gif` 경로
- 검수 시각: 2026-09-25 00:27 KST
- 배포 포함 파일: 릴리스 커밋 `646210c0eb0a5dc7518cd96d4d79627b550b0f00`의 Git 추적 파일 54개. 이 사후 증거 보고서와 `.git`, 무시 파일은 실행 번들 해시에서 제외한다.
- 대표 요청: “DesignHub용 겨울 눈사람이 손을 흔드는 투명 GIF 요소를 만들고 업로드 전 CSV를 준비해줘.” 동일한 사용자 제공 베이스 PNG와 `evals/fixtures/winter-snowman-wave.json`을 두 실행에 복사한다.
- 기대 산출물: 독립 실행마다 768×768, 서로 다른 4프레임, 무한 루프, 투명 배경, 25 MB 미만인 GIF; 원본 행·RGBA 프레임·아틀라스·매니페스트·검수 보고서; `fileName=wave`, 빈 `uniqueId`, `Premium`, `GIF`, 고유 검색어 20–25개의 사전 CSV. 외부 업로드는 하지 않는다.
- 탐색 경계: 각 새 임시 홈의 `plugins/imagen-design-hub`만 배포 루트로 삼는다. 최대 깊이 6, Git 추적 파일 포함, `.git`·무시 파일·이 보고서 제외, 심링크는 따르지 않음, 상대 경로 사전순 처리. 실제 최대 깊이는 3이다.
- 허용 변동: 임시 절대경로, 생성 시간, 모델이 만든 픽셀·포즈·파일 바이트·파일 크기. 루트·배포 파일 집합·입력 해시·제공자·단계·상대 산출물 경로·프레임 수·규격·판정은 같아야 한다.
- PASS 조건: 두 새 환경에서 설치·활성화·오류 입력·실제 GIF 생성·시각/수치 검수·제거가 성공하고, 두 판단 계약이 일치하며 차단 결함이 없어야 한다.

## 정적 검사

### 파일 참조

| 참조 | 읽는 단계 | 생성 단계 | 배포 포함 | 판정 | 증거 |
|---|---|---|---|---|---|
| `SKILL.md` → `skills/gif/SKILL.md`와 한국어본 | 라우팅 | 해당 없음 | 예 | PASS | 두 번들에 새 경로 존재, `gif-beta` 경로 없음 |
| GIF 스킬 → 공통 규칙·`upload-csv` | GIF·메타데이터 | 해당 없음 | 예 | PASS | Markdown 로컬 링크 검사 |
| 스킬·참조 문서의 로컬 링크 전체 | 해당 작업 | 해당 없음 | 예 | PASS | 50개 확인, 누락 0개 |
| `evals/fixtures/winter-snowman-wave.json` | `prepare` | 해당 없음 | 예 | PASS | 두 번들 동일 SHA-256 `6f79aa3f3bff9f781d3054dcc76ab79186bbe337fa8c83fddc974c4072f1f3ce` |
| 베이스 PNG → 원본 행·프레임·GIF | 생성 | 실행 중 생성 | 사용자 제공 입력 | PASS | 베이스 SHA-256 `d58301e49ffe03a94dad8f65a9f10f904cf218a78f35f46cfeb13e3497cc4932` |

### 의존성

| 의존성 | 포함/생성/사용자 제공 | 안내 위치 | 판정 | 증거 |
|---|---|---|---|---|
| 플러그인 manifest·스킬·설치기·검수 fixture | 포함 | `README.md`, `SKILL.md` | PASS | 각 번들 54개, 동일 해시 `f2ecc1dafada862a611a98a319cafdf933f0e08e1f17c5fe19d99c845300319c` |
| Node 18+·Git·Codex CLI | 사용자 제공 | README 설치 절차 | PASS | 두 새 홈에서 등록·설치·목록·제거 실행 |
| sprite-gen 2.7.0과 전용 venv | 사용자 제공 | README와 `skills/gif/SKILL.md` | PASS | 설치본 `SKILL.md`와 `pyproject.toml` 버전 확인, 각 실행에서 전체 행 파이프라인 완료 |
| Codex 이미지 생성 접근 | 사용자 제공 | sprite-gen `user-workflow`, GIF 스킬 | PASS | `--provider codex` 명시, 양쪽 행 생성 성공. 계정 인증은 외부 제공, 개인 메모리·기존 run은 입력으로 쓰지 않음 |
| 원본 행·프레임·아틀라스·GIF·CSV | 생성 | GIF 스킬·공통 규칙 | PASS | 각 run의 상대 파일 구조 25개 일치 |
| Computer Use·DesignHub 로그인 | 실제 업로드 때 사용자 제공 | `upload-csv` | 범위 밖 | 이번 검수는 업로드 전 후보까지만 수행 |

로컬 GIF 인코더는 `ffmpeg -encoders`에서 소프트웨어 `gif`만 확인됐다. VideoToolbox는 H.264/HEVC/ProRes에만 나타나므로 sprite-gen의 CPU GIF 합성을 사용했다. Codex 원격 이미지 생성의 백엔드 하드웨어 종류는 도구가 반환하지 않아 단정하지 않는다.

### 설치와 활성화

| 항목 | 문서 위치 | 실제 확인 방법 | 판정 |
|---|---|---|---|
| 복사 위치 | 양국어 README | 새 홈의 `plugins/imagen-design-hub`에 배포 파일만 복사 | PASS |
| 마켓플레이스·설치 | 양국어 README | 등록 → 필요한 경우 `codex plugin marketplace add <새 홈>` → `codex plugin add imagen-design-hub@personal` | PASS, 두 번 |
| 런타임·권한 | README 의존성 | Node·Codex·sprite-gen 실행, 파일 생성 | PASS |
| 재로드·인식 | README 새 작업 안내 | `codex plugin list`가 0.5.1 installed/enabled 표시. 별도 새 Codex 작업이 `imagen-design-hub:gif`를 선택 | PASS |
| 제거 방법 | 양국어 README | `codex plugin remove` → 번들 등록 해제 → 목록에서 사라짐 | PASS, 두 번 |

최종 live Codex 라우팅 검사에서는 `imagen-design-hub:gif`로 답했고 `defaultPrompt` 경고가 없었다. 별도 작업은 현재 계정의 인증을 사용했으며 파일 생성·수정은 금지했다.

## 테스트 1: 콜드 스타트 인수

- 새 환경: `/tmp/idh-051-winter-finalpass.Zye6GL/one`; 전용 HOME·CODEX_HOME·SPRITE_GEN_CONFIG_DIR. 배포 파일 54개만 복사하고 동일한 베이스 입력을 `input/base.png`에 둠.
- 실행: `register_marketplace.mjs` → `codex plugin marketplace add` → `codex plugin add` → `sprite-gen workflow --kind sprite --base-image … --motion-method gpt-rows --confirmed-access codex` → `prepare --request … --chroma-key '#FF00FF' --no-fit-pixel-unfake` → `gen-set --provider codex --concurrency 1` → `extract` → `compose-atlas` → `compose-gif` → `inspect` → CSV/재생 검수 → 제거.
- 관찰: `workflow.status=ready`, 행 생성 OK(106.2초), `extract.errors=[]`, `inspect.errors=[]`, `inspect.warnings=[]`. GIF 768×768, 4개 서로 다른 프레임, 각 250 ms, 무한 루프, 이진 투명, 482,511 B. CSV 1행·고유 검색어 23개. 전체 프레임과 흰색·어두운색·체커 배경을 직접 확인했다.
- 산출물 보존: `/Volumes/ssd/Codex/miricanvas-design/outputs/2026-09-25-00-25-07-winter-productization-051-pass/test-one/`; GIF SHA-256 `074e8dc0b137150565449a4adec8a6c6f93a8a1acba9cdb90335dc611616bc2b`.
- 잘못된 입력: 없는 `input/missing.png`을 베이스로 지정한 `prepare`가 종료 코드 1과 `missing base image`를 반환. `bad-run/sprite-request.json`은 생성되지 않았다.
- 판정: `PASS`

## 테스트 2: 반복 일관성

- 별도 새 환경: `/tmp/idh-051-winter-finalpass.Zye6GL/two`; 첫 실행의 HOME·상태·run을 재사용하지 않음.
- 실행 명령·입력·제공자·단계·오류 입력 검사는 테스트 1과 동일.
- 관찰: `workflow.status=ready`, 행 생성 OK(86.7초), 추출/검수 errors와 warnings 빈 배열. GIF 768×768, 서로 다른 4프레임, 각 250 ms, 무한 루프, 이진 투명, 492,005 B. CSV 1행·고유 검색어 23개. 전체 프레임과 세 배경 검수 통과.
- 산출물 보존: `/Volumes/ssd/Codex/miricanvas-design/outputs/2026-09-25-00-25-07-winter-productization-051-pass/test-two/`; GIF SHA-256 `48c0fc31476f4a42167af303aebd6a96be77fb11d0a4ff4ef862dc7a5f1369b6`.
- 잘못된 입력: 같은 `missing base image` 오류, 종료 코드 1, 잘못된 요청서 미생성.

| 비교 항목 | 실행 1 | 실행 2 | 허용 변동 | 판정 |
|---|---|---|---|---|
| 탐색 루트·깊이·파일 집합 | 플러그인 루트, 최대 6, 54개, 위 번들 해시 | 동일 | 임시 부모 경로 | PASS |
| 포함·제외·처리 순서 | Git 추적 파일, 무시 파일 제외, 상대 경로 사전순 | 동일 | 없음 | PASS |
| 선택 입력 | 베이스·요청서 해시 동일 | 동일 | 없음 | PASS |
| 실행 분기 | Codex GPT 행, 마젠타 키, 동일한 5단계와 inspect | 동일 | 생성 픽셀·시간 | PASS |
| 산출물 구조 | 25개 상대 파일, `previews/wave.gif`, `preupload.csv` 등 | 동일 | 파일 바이트 | PASS |
| 최종 판정 | PASS | PASS | 없음 | PASS |

- 판정: `PASS`

## 발견한 결함과 수정

| 심각도 | 결함 | 재현 증거 | 수정 | 재검증 증거 |
|---|---|---|---|---|
| 높음 | 기존 설치 안내의 임의 복제 위치가 등록기의 `./plugins/imagen-design-hub` 경로와 맞지 않음 | 초기 새 홈에서 `plugin source path is not a directory` | 양국어 README에 정확한 복제·마켓플레이스·제거 절차 기재 | 최종 두 새 홈의 설치·제거 성공 |
| 높음 | Codex가 기존 기본 프롬프트 129자와 4개 목록을 일부 무시 | 새 Codex 작업의 `at most 128 characters`, `maximum of 3 prompts` 경고 | 3개로 병합, 길이 122/111/108자 | 새 Codex 작업에서 `gif` 라우팅, 해당 경고 0개 |
| 중간 | 이름만 바꾸면 옛 `gif-beta` 빈 디렉터리로 플러그인 검증 실패 | `skill gif-beta is missing SKILL.md` | 옛 경로 제거, 문서·UI·agent prompt를 `gif`로 통일 | 번들에서 옛 스킬 없음, 플러그인/스킬 검증 통과 |
| 중간 | 최초 겨울 fixture의 특정 팔 방향은 생성형 모델에서 다르게 해석됨 | 초기 두 GIF의 팔 방향 불일치 | 동작 의미를 유지하며 “one twig arm”으로 명시 | 동일 fixture를 사용한 최종 두 실행에서 손 흔들기와 계약 통과 |

수정마다 실패한 폴더를 이어 쓰지 않고 새 임시 홈 두 개에서 전체 경로를 다시 실행했다. 최종 PASS 근거는 마지막 `winter-finalpass` 실행만 사용한다.

## 최종 판정

`PASS`

- [x] 서로 다른 새 환경에서 실제 GIF 생성까지 두 번 실행했다.
- [x] 유령 파일·누락 링크·미선언 필수 의존성이 없다.
- [x] 설치·활성화·새 작업의 경로 인식·제거를 확인했다.
- [x] 탐색 경계·순서·입력 해시·실행 분기·필수 산출물 구조가 일치한다.
- [x] 두 GIF의 프레임·투명도·루프·규격·CSV·시각 검수를 확인했다.
- [x] 오류 입력에서 임의 값을 만들지 않고 실패했다.

이 판정은 플러그인의 겨울 GIF 후보 제작 경로에 한정한다. DesignHub 실제 업로드·심사 승인과 최신 사이트 수용 규칙은 이번에 확인하지 않았고, 두 GIF는 업로드 전 후보이다.

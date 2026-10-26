# Codex 이미지 생성 조건과 진단

[English](image-generation-troubleshooting.md)

네이티브 PNG/JPG 생성 경로에 적용한다. 플러그인은 지침을 제공하며 이미지 서비스나 계정 권한을 추가하지 않는다.

## 계정·세션

- **Codex Free 플랜:** 내장 이미지 생성은 지원되지 않는다. 무료 Codex 코딩이나 ChatGPT 웹 이미지 권한을 Codex 이미지 권한으로 해석하지 않는다. 공식 [가격 FAQ](https://developers.openai.com/codex/pricing/)를 확인한다.
- **지원되는 ChatGPT 로그인:** 내장 경로에는 `OPENAI_API_KEY`가 필요 없다. 사용 한도·워크스페이스 정책은 별도다. 도구가 없다는 이유로 로그인을 바꾸거나 키를 요청하지 않는다.
- **제공자·모델:** 이미지 생성 기능, 이미지 지원 제공자·모델, Codex 백엔드 인증이 필요하다. API 키 전용 로그인은 별도 경로이며 키를 추가한다고 누락된 내장 도구가 활성화되지는 않는다. 버전이 고정된 [등록 조건](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/core/src/tools/spec_plan.rs)과 [인증 방식](https://github.com/openai/codex/blob/rust-v0.162.0/codex-rs/protocol/src/auth.rs)을 참고한다.
- **실제 목록:** 지연 로딩 도구도 확인한다. `image_generation`은 기능 플래그이고 `image_gen`은 네임스페이스다. `image_gen__imagegen`처럼 노출되기도 하므로 문자 그대로의 함수명 불일치만으로 없다고 단정하지 않는다.

Windows나 `codex exec`를 일괄 미지원으로 분류하지 않는다. 별도의 비무료 시험 계정에서 ChatGPT 로그인 상태의 앱 번들 CLI `0.164.0-alpha.11.1`로 Windows `codex exec` 실제 생성을 확인했다([실기 증거](../records/2026-10-26-issue-1-investigation.md)). 신고자의 환경이나 Free 계정 성공을 입증한 것은 아니다. `0.162.0` 소스에도 도구가 있다. 이는 확인한 버전이지 **최소 지원 버전 입증은 아니다**. 앱 빌드 번호와 CLI 버전은 서로 다르다.

## Windows 설치

문제가 발생한 동일 PowerShell 터미널에서 실행한다.

```powershell
Get-Command codex -All
where.exe codex
codex --version
```

`codex`를 찾지 못하면 데스크톱 앱이 설치돼 있어도 그 터미널에서는 실행할 수 없다. 공식 [CLI 설치 안내](https://github.com/openai/codex#installing-and-running-codex-cli)에 따라 설치하고 터미널을 다시 연 뒤 재확인한다. 플러그인 설치기는 이 플러그인을 설치·등록할 뿐 Codex CLI를 설치하지 않는다. 공식 npm 방식을 선택하면 Windows에서 `npm.cmd install -g @openai/codex`로 호출할 수 있으며 Node·npm이 먼저 있어야 한다.

별도 설치 없이 진단할 때 Microsoft Store 앱에 CLI가 포함돼 있을 수 있다.

```powershell
$app = Get-AppxPackage OpenAI.Codex | Select-Object -First 1
if (-not $app) { throw "Codex Store package not found; use the official CLI install instructions." }
$cli = Join-Path $app.InstallLocation 'app\resources\codex.exe'
if (-not (Test-Path $cli)) { throw "Bundled CLI path differs; use the official CLI install instructions." }
& $cli --version
& $cli login status
& $cli features list | Select-String 'image_generation'
```

GUI `Codex.exe`가 아니라 `resources\codex.exe`를 쓴다. 관찰한 구조이지 모든 설치에 보장되지는 않는다. 버전이 들어간 WindowsApps 경로를 고정하지 않는다. 이 실행 파일을 진단하는 경우 이후 명령의 `codex`를 `& $cli`로 바꾼다.

이미 `codex exec`가 완료됐다면 해당 호출에는 실행 가능한 CLI가 있었다. 다른 터미널의 PATH 누락만으로 원인을 단정하지 말고 경로·버전을 비교한다. Windows 네이티브·WSL·데스크톱 번들 CLI를 구분한다.

## 도구 미제공 시 조치

비밀정보 없는 진단 출력을 수집한다.

```powershell
codex --version
codex login status
codex features list | Select-String 'image_generation'
codex plugin list
```

POSIX 셸에서는 `grep image_generation`을 쓴다. 플랜은 계정·사용량 UI에서 확인하고 선택된 모델·제공자도 확인한다. 토큰·`auth.json`·API 키·전체 개인 설정을 붙여넣지 않는다.

1. 실행 파일과 ChatGPT/API 키 전용 로그인 여부를 확인한다. 플랜은 관찰한 경우만 기록하고 Free라면 공식 Codex 이미지 제한을 설명한다.
2. `image_generation`이 있지만 false라면 `codex exec --enable image_generation "Report whether the native image tool is exposed; do not generate an image."`로 해당 호출만 시험할 수 있다. 계정·제공자·모델 제한을 우회하지는 못한다. 알 수 없는 플래그라면 설정을 지어내지 말고 공식 방식으로 해당 CLI를 갱신한다.
3. 플래그가 true인데 도구가 없으면 플랜·제공자·모델·워크스페이스 정책을 확인한다. 필요하면 해당 클라이언트를 갱신하고 플러그인 버전을 확인한 뒤 새 작업을 시작한다. 플러그인 재설치만으로 호스트 권한은 추가되지 않는다.
4. 도구가 있지만 호출에 실패하면 정확한 오류를 보존하고 인증·접근 거부, 사용 한도·요청 제한, 파일시스템·샌드박스 실패를 구분한다. 모두 도구 누락으로 분류하지 않는다. 작업 폴더 복사가 거부돼도 `$CODEX_HOME/generated_images/`(기본 `~/.codex/generated_images/`)에 원본이 있을 수 있다. 원본 생성과 복사·후처리 성공을 구분한다.
5. 해결되지 않으면 실행 명령, 앱·CLI 각각의 버전, 로그인 방식, 관찰했거나 추가 확인할 플랜, 기능 값, 모델·제공자, 실제 도구명 또는 부재, 정확한 오류를 보고한다. 다른 시험 컴퓨터의 계정을 신고자의 계정으로 추정하지 않는다.

유료 대안 실행 전에 멈춘다. 설치된 imagegen 스킬의 CLI/API 대안은 API 키와 사용자의 명시적 선택이 필요하며 API 과금은 별도다. 브라우저 생성도 명시적 대안일 때만 쓰고 자동 실행하지 않는다. 업그레이드만이 유일한 조치라고 요구하지 않는다. 네이티브 생성 없이 가능한 추천·사용자 제공 원본 처리는 요청 범위 안에서 계속할 수 있다.

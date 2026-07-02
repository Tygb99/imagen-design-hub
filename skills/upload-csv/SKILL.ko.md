---
name: upload-csv
description: MiriCanvas 또는 DesignHub 요소 파일이 업로드 준비된 뒤, Aside(macOS), 사용 가능한 MCP, 또는 명시적으로 확인된 UI 경로 같은 live DesignHub surface로 파일 업로드, CSV 메타데이터 다운로드, uniqueId 보존 병합, CSV 재업로드를 진행할 때 사용한다.
---

# Imagen Design Hub: 업로드 후 CSV

[English version](SKILL.md)

사용자가 `요소 업로드후 csv업로드`, `uplode-csv`, `upload-csv`, DesignHub upload CSV, metadata upload, CSV merge, uniqueId preservation, post-upload DesignHub metadata를 말하면 이 경로를 사용한다.

이 스킬은 파일 업로드 이후의 메타데이터 단계다. DesignHub 최종 심사 제출을 조용히 진행하면 안 된다.

공유 참고자료: route별 `contentType` 값과 keyword rule이 필요하면 `../../SKILL.ko.md`를 읽는다.

## 필수 Live Surface

DesignHub UI를 실제로 조작하는 모든 단계는 사용자가 요청한 surface를 사용한다.

- 사용자가 Aside를 요청하면 `aside-browser`를 사용한다. Aside는 현재 macOS에서만 지원된다. Windows 지원은 예정이므로 Windows Aside 지원을 있다고 말하거나 가정하지 않는다.
- 다음 우선 자동화 경로는 MCP다. DesignHub MCP 도구가 사용 가능하고 사용자가 요청하면 browser UI 대신 MCP로 upload/download action을 수행한다.
- 사용자가 다른 surface를 지정한 뒤에는 Chrome, Computer Use, 숨은 browser automation, direct HTTP call, hidden API, terminal-only shortcut으로 바꾸지 않는다.
- Chrome 또는 Computer Use는 사용자가 명시적으로 요청했거나, 특정 surface 요청이 없고 해당 경로가 확인된 지원 경로일 때만 사용한다.
- 로컬 CSV 병합, 행 검증, encoding 검사, 파일 검사는 일반 filesystem과 terminal 도구를 사용해도 된다.
- 파일 업로드와 CSV 메타데이터 전송은 외부 DesignHub 상태를 바꾸므로, 특정 파일과 대상에 대한 확인이 아직 없었다면 live action 전에 사용자 확인이 필요하다.
- 사용자가 별도 외부 제출 단계를 명시적으로 요청하지 않았다면 최종 심사 제출은 절대 누르지 않는다.

## 필수 순서

1. 사용자가 외부 DesignHub action을 명시적으로 확인한 경우에만, 확인된 live surface로 준비된 image/vector/GIF 파일을 업로드한다.
2. DesignHub가 `10 of 10 uploaded` 같은 업로드 완료 상태를 보일 때까지 기다린 뒤 업로드 완료로 본다.
3. 같은 확인된 live surface로 파일 업로드 후 DesignHub가 제공하는 CSV를 다운로드한다.
4. 다운로드한 CSV를 `fileName`과 `uniqueId`의 source of truth로 취급한다.
5. 준비한 metadata를 다운로드한 행에 병합하되 `uniqueId`를 삭제하거나, 불필요하게 재정렬하거나, 다시 만들지 않는다.
6. 병합 CSV는 새 batch 행만이 아니라 다운로드한 DesignHub CSV의 모든 행을 유지한다.
7. 로컬 프로젝트 계약이 quote-all CSV를 요구하면 CSV는 UTF-8 without BOM, 모든 field quote 상태로 유지한다.
8. 사용자가 해당 외부 action을 명시적으로 확인한 경우에만, 확인된 live surface로 병합 CSV를 다시 업로드한다.
9. CSV 업로드 후 DesignHub 완료 메시지나 배너를 확인한다. 처리된 행 수를 기록하고, 파일 업로드, CSV 업로드, 최종 심사 제출을 구분한다.

파일 등록 후 로컬 preupload CSV를 바로 올리지 않는다. DesignHub는 파일 업로드 후에만 `uniqueId`를 부여하므로, 올바른 흐름은 항상 현재 DesignHub CSV를 다운로드하고, 그 전체 파일에 병합한 뒤, 병합한 전체 CSV를 업로드하는 것이다.

## Content Type 값

공식 CSV 값을 정확히 사용한다.

```text
Photo
Photo(Cut-out)
SVG element
PNG element
GIF
Background
```

`JPG background`라고 쓰지 말고 `Background`를 사용한다.

## 메타데이터 규칙

- JPG background, SVG, GIF 행의 `fileName`은 보통 확장자 없는 basename이다.
- PNG element flow에서는 DesignHub에서 다운로드한 CSV가 기대하는 값을 따르고, 최종 upload basename을 실제 파일과 맞춘다.
- `uniqueId`는 DesignHub에서 다운로드한 CSV 값을 보존한다.
- 사용자가 다르게 말하지 않으면 `tier`는 `Premium`이다.
- `keywords`는 20~25개의 고유한 구매자 검색어여야 한다.
- `Photopea`, `imagegen`, `PNG`, `JPG`, `SVG`, `GIF`, `CSV`, `Premium`, `DesignHub`, `MiriCanvas`, run ID, 날짜 같은 제작/관리 용어는 사용자가 명시적으로 요구하지 않으면 제거한다.

## 검증

준비 완료를 보고하기 전에 확인한다.

- 행 수가 DesignHub에서 다운로드한 CSV와 일치한다.
- 다운로드한 CSV의 모든 `uniqueId` 값이 보존되었다.
- 모든 최종 `fileName` 값이 업로드된 파일과 매칭된다.
- 병합 CSV는 새 batch 행만이 아니라 다운로드한 DesignHub CSV의 모든 행을 유지한다.
- `contentType` 값이 공식 목록에 있다.
- 각 행 안에 중복 keyword가 없다.
- keyword 수가 행마다 20~25개다.
- CSV encoding은 UTF-8 without BOM이다.
- 로컬 프로젝트 계약이 quote-all CSV를 요구하면 모든 field가 quote되어 있다.
- DesignHub 파일 업로드, CSV 다운로드, CSV 업로드가 사용자가 요청한 surface에서 수행되었다.
- Aside 사용은 macOS로 제한되었거나, MCP/다른 지원 경로가 명시적으로 선택되었다.
- DesignHub가 성공 처리 행 수를 표시했거나 오류 메시지를 그대로 캡처했다.
- DesignHub가 예상 업로드 수와 CSV 처리 행 수를 보고했다.
- 파일 업로드, CSV 업로드, 최종 심사 제출이 실제로 일어났는지 분명히 보고한다.

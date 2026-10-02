---
name: upload-csv
description: Aside에서 준비된 DesignHub 파일을 업로드하거나 기존 제출 예정 항목을 처리하고, 부여된 uniqueId를 보존해 CSV 메타데이터를 등록하며 승인 범위 안에서 심사 제출한다.
---

# Imagen Design Hub: 업로드 후 CSV

[English version](SKILL.md)

사용자가 `요소 업로드후 csv업로드`, `uplode-csv`, `upload-csv`, DesignHub upload CSV, metadata upload, CSV merge, uniqueId preservation, post-upload DesignHub metadata를 말하면 이 경로를 사용한다.

준비된 파일 또는 사용자의 기존 제출 예정 항목에서 시작한다. 파일 업로드·메타데이터 등록·심사 제출은 각각 선택한 항목과 목적지를 포함하는 승인이 필요하며, 이미 받은 승인은 계속 유효하다.

공유 참고자료: route별 `contentType` 값과 keyword rule이 필요하면 `../../SKILL.ko.md`를 읽는다.

## 브라우저와 파일 지정

- DesignHub는 Aside REPL을 우선한다. 설치된 Aside 스킬과 현재 가이드를 읽고, 해당하는 기존 탭에 연결한 뒤 현재 페이지를 확인해 컨트롤을 찾는다.
- 이미지·벡터·GIF 파일과 병합 CSV는 확인한 파일 입력칸의 `setInputFiles()`를 우선한다. 대량 작업은 1,000개 파일 경로를 한 묶음으로 잡되, 실제 업로드 한도나 사용자가 요청한 더 작은 수량에 맞춰 줄인다. 이 수량은 작업 단위이며 DesignHub의 최대 허용 수량을 뜻하지 않는다.
- 파일 직접 지정이 지원되지 않거나 실패하면 Computer Use로 브라우저의 파일 선택 창을 조작한다. 열기 전에 선택 파일을 다시 확인한다. 필요한 경우에만 사용자의 선택에 맞게 브라우저를 전환한다.
- CSV는 브라우저 다운로드 기능을 사용한다. 저장 대화상자가 나타날 때만 Computer Use로 처리하고, 완료된 다운로드 파일을 확인한 뒤 병합한다.
- 로컬 CSV 병합과 파일 검사는 파일 도구를 사용할 수 있다. 함수가 있거나 파일이 선택됐다는 사실만으로 업로드 성공을 보고하지 않고 DesignHub의 완료 상태를 확인한다.
- 실패 항목은 최초 시도 후 최대 2회 재시도하고 계속 실패하면 건너뛰어 나머지를 처리한다. 업로드·제출 응답이 불분명하면 중복을 막기 위해 재시도 전에 현재 상태를 확인한다.

## 필수 순서

1. 대상 파일 또는 기존 제출 예정 항목과 승인 범위를 확인한다. 준비된 파일은 Aside로 업로드하고, 이미 등록된 항목을 처리할 때는 파일 업로드를 건너뛴다. 무관한 항목은 선택에서 제외한다.
2. 새 파일을 업로드했다면 DesignHub가 `10 of 10 uploaded` 같은 업로드 완료 상태를 보일 때까지 기다린 뒤 업로드 완료로 본다.
3. 제출 예정/대상 목록으로 이동해 그 화면의 CSV 다운로드 컨트롤을 사용한다. 관리 페이지의 `업로드된 모든 콘텐츠` export에 pending 파일이 포함된다고 가정하지 않는다.
4. CSV 다운로드 완료를 확인하고 로컬에서 검사한다. 저장 대화상자가 나타나면 timestamp가 붙은 명시적 파일명으로 저장한다.
5. 선택한 다운로드 CSV에 새로 업로드한 모든 basename이 있고 각 `uniqueId`가 비어 있지 않은지 확인한 뒤, 그 CSV를 `fileName`과 `uniqueId`의 source of truth로 취급한다.
6. 준비한 metadata를 다운로드한 행에 병합하되 `uniqueId`를 삭제하거나, 불필요하게 재정렬하거나, 다시 만들지 않는다.
7. 병합 CSV는 새 batch 행만이 아니라 다운로드한 DesignHub CSV의 모든 행을 유지한다.
8. 로컬 프로젝트 계약이 quote-all CSV를 요구하면 CSV는 UTF-8 without BOM, 모든 field quote 상태로 유지한다.
9. 이미 받은 승인 범위 안에서 Aside로 병합 CSV를 다시 업로드한다. 같은 항목과 목적지를 포함하는 승인을 반복해서 묻지 않는다.
10. CSV 업로드 후 DesignHub 완료 메시지나 배너를 확인한다. 처리된 행 수를 기록하고, 파일 업로드, CSV 업로드, 최종 심사 제출을 구분한다.
11. AI로 생성한 소재는 생성형 AI 표시를 체크하고 저장한다. 개별 제목·키워드를 덮어쓰지 않고 저장된 상태를 확인한다.
12. 심사 제출이 승인됐다면 현재 페이지의 허용 수량에 맞춰 대상 항목만 나누어 제출한다. 제출 예정에서 심사 대기로 이동했는지 확인한다. 파일 지정 단위는 심사 허용 수량과 별개다.

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
- `imagegen`, `PNG`, `JPG`, `SVG`, `GIF`, `CSV`, `Premium`, `DesignHub`, `MiriCanvas`, run ID, 날짜 같은 제작/관리 용어는 사용자가 명시적으로 요구하지 않으면 제거한다.

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
- 선택한 파일·부여된 ID·목적지가 승인된 작업 묶음과 일치한다.
- AI로 생성한 소재의 생성형 AI 표시가 저장되었다.
- DesignHub가 성공 처리 행 수를 표시했거나 오류 메시지를 그대로 캡처했다.
- DesignHub가 예상 업로드 수와 CSV 처리 행 수를 보고했다.
- 파일 업로드, CSV 업로드, 최종 심사 제출이 실제로 일어났는지 분명히 보고한다.

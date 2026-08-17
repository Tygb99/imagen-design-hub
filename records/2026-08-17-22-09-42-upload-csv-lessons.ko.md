# 2026-08-17 upload-csv 실행 함정 기록

JPG 배경 4개를 업로드하고 DesignHub 전체 CSV를 등록하는 과정에서 확인한 운영 함정이다.

## 확인된 순서

- DesignHub `Background` 경로에서 JPG 4개를 업로드했다.
- 관리 페이지의 `업로드된 모든 콘텐츠` export는 active/manage 189행만 반환했고 새 pending basename은 포함하지 않았다.
- 제출 예정 목록의 CSV 다운로드는 275행을 반환했고 새 4개 basename과 비어 있지 않은 `uniqueId`를 포함했다.
- 병합 CSV는 275행과 275개 `uniqueId`를 모두 보존했다. DesignHub는 `모든 행(275행)을 처리했습니다.`라고 표시했다.
- 최종 심사 제출은 의도적으로 진행하지 않았다.

## 함정과 수정 절차

1. 관리 페이지가 아니라 제출 예정/대상 목록의 CSV export를 선택한다. 대상 목록 행 수와 맞추고 새 basename이 모두 있는지 확인한다.
2. CSV 다운로드가 시작된 뒤 macOS 저장 대화상자를 끝까지 완료한다. `.com.google.Chrome.*` 파일은 이름을 지정해 저장하고 로컬 검사하기 전에는 임시 파일로 취급한다.
3. 파일 선택기가 Finder처럼 보이는 상태에서 Chrome `열기` 상태로 바뀔 수 있으므로 Computer Use의 active app state를 매번 다시 조회한다.
4. Go To Folder에 정확한 폴더 또는 파일 경로를 입력한다. 목표 파일의 selected 표시와 `열기` 버튼 활성화를 확인한다. 이 선택기에서는 무조건 `Cmd+A`를 누르는 방식이 불안정하다.
5. 파일 업로드 성공과 CSV 처리 완료는 심사 승인과 다르다. 피사체가 보이는 이미지는 `Background` 타입으로 처리되어도 Background 심사 기준을 위반할 수 있다.

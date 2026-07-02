---
name: png-element-full-workflow-ko
description: MiriCanvas와 DesignHub PNG 요소 생성, chroma-key cleanup, Photopea 마무리, magenta-fringe QA, CSV 검증 전체 workflow.
---

# PNG 요소 전체 Workflow

MiriCanvas / DesignHub용 투명 스티커, 일러스트, 오브젝트, cutout, PNG 요소, 배경 제거, Photopea 마무리, 업로드용 alpha asset에 이 workflow를 사용한다.

## Route Triggers

사용자가 아래 항목 중 하나를 말하면 `png-element` route를 사용한다.

- `png요소`, PNG element, sticker, cutout, transparent PNG, alpha asset
- background removal, chroma key, Photopea, upload-ready PNG
- key 제거 후 magenta/purple fringe cleanup

요청이 JPG background, SVG/GIF route, DesignHub CSV upload, plugin-wide routing으로 넘어가면 `../../SKILL.ko.md`를 읽는다.

## Core Rules

- source 생성에는 설치된 `$image-gen` 스킬을 사용해 새 `codex exec` 세션에서 생성한다. 내부 이미지 도구는 built-in `image_gen`이다.
- 완전히 평평한 단색 chroma-key 배경으로 생성한다.
- imagegen에 투명 배경이나 체크보드 배경을 요청하지 않는다.
- key color는 피사체와 겹치지 않는 색을 고른다. 피사체가 비슷한 보라색을 쓰지 않을 때만 `#8000ff`를 기본값으로 쓴다. 초록 피사체에는 magenta를 쓰고, 파란 피사체에는 blue를 피한다.
- imagegen 프롬프트에 key color를 피사체 내부에 쓰지 말라고 명시한다.
- key가 magenta 또는 purple이고 피사체 안에 pink, purple, magenta를 의도적으로 쓰지 않는다면 alpha 추출 뒤 magenta-fringe decontamination을 실행한다.
- 피사체에 실제 pink, purple, magenta 디테일이 있다면 magenta-fringe decontamination을 실행하지 않는다. 더 안전한 key color를 고르거나 해당 디테일을 mask로 보존한다.
- 바람, breeze, 공기 흐름, 안개, 유리, 물보라, motion line 같은 반투명 효과는 배경색 테스트만으로 부족하다. 효과 안에 key color가 끼면 더 안전한 key로 다시 생성하거나, key 제거 전에 효과 주변에 의도적인 밝은색/중립색 outline 또는 stroke를 넣는다.
- 독립 PNG 요소를 여러 개 만들 때는 요소마다 source 이미지를 따로 생성한다. 여러 요소를 한 장에 몰아 만든 뒤 잘라 쓰지 않는다. 분리 후 확대하면 계단현상과 약한 anti-aliasing이 드러날 수 있다.
- source 파일은 `assets/source-imagegen/`에 보존한다.
- 먼저 `../../scripts/chroma_key.py`를 실행해 `assets/raw/`로 출력한다.
- DesignHub PNG 요소 작업에는 `.system/imagegen/remove_chroma_key.py`를 사용하지 않는다.
- 사용자가 비교나 fallback을 명시적으로 요청하지 않으면 `../../scripts/remove_chroma_key.py`를 사용하지 않는다.
- 업로드용 DesignHub PNG는 Photopea 또는 프로젝트 Photopea runner를 거쳐 `assets/processed/`로 마무리한다.
- review contact sheet는 검토용 산출물일 뿐이다. 최종 업로드 PNG를 contact sheet에서 잘라 만들지 않는다.

## Chroma-Key Workflow

명령은 `skills/png-element/`에서 실행한다. plugin root에서 실행한다면 path를 조정한다.

edge-connected cleanup으로 실행한다.

```bash
python ../../scripts/chroma_key.py \
  --input "<source.png>" \
  --output "<raw-alpha.png>" \
  --background "<KEY_COLOR>" \
  --tolerance 48 \
  --scope edge \
  --dpi 350
```

피사체 내부의 key color와 가까운 디테일이 사라지면 tolerance를 넓히지 말고 더 안전한 배경색으로 다시 생성한다.

넓은 global tolerance보다 edge-connected 제거를 우선한다. global tolerance는 선풍기, 오브젝트, 패턴 내부의 색이 key color와 가까울 때 피사체 디테일을 같이 지울 수 있다. 내부 디테일이 손상되면 enclosed removal을 낮추거나 더 안전한 key color로 다시 생성한 뒤 결과를 채택한다.

chroma-key 제거와 Photopea 마무리 후에는 체크보드, 흰색, 어두운 배경에서 edge를 확대 검수한다. outline이 아직 계단형이거나 jagged하면 원래 per-element source에서 finishing을 다시 하거나 요소별로 다시 생성한다. 로컬에서 확대한 crop을 upload-ready로 받아들이지 않는다.

## Magenta Fringe Decontamination

magenta 또는 purple key-color run에서 프롬프트가 피사체 내부의 pink, purple, magenta 사용을 금지한 경우에만 사용한다. 이 단계는 anti-aliased edge에 남은 key-color 오염을 없애는 후처리이며 일반 색보정이 아니다.

alpha 추출 뒤, 최종 Photopea/contact-sheet 승인 전에 alpha가 0보다 큰 visible pixel을 검사한다. `red > green`이고 `blue > green`인 픽셀은 magenta cast로 본다. 해당 픽셀의 RGB를 `(green, green, green)`으로 바꾸고 alpha는 그대로 유지한다.

적용 전후 count를 확인한다. 남은 visible magenta-cast pixel 수가 `0`이고, transparent-pixel RGB가 깨끗하며, 어두운 preview(`#282828`)에서 보라 outline이 보이지 않을 때만 채택한다. 흰색과 체크보드 preview도 함께 확인한다.

magenta가 아닌 key에는 더 안전한 key color 또는 재생성을 우선한다. 실제 피사체 색을 몰래 channel-neutralization하지 않는다.

## Output Contract

- 최종 업로드 후보는 alpha가 있는 PNG 파일이다.
- 프로젝트가 다르게 말하지 않으면 tight alpha bbox를 사용한다.
- 현재 MiriCanvas DesignHub 제출 흐름에서는 최종 PNG를 350 DPI, 한 변 최소 2500 px로 유지한다.
- CSV 행의 `contentType` 값은 `PNG element`다.
- 키워드는 20~25개의 고유한 구매자 검색어여야 한다.
- 키워드는 plugin-wide guide인 `../../../references/keyword-generation.ko.md`를 기준으로 만든다. 대상/사물, 요소 형식, 스타일, 용도, 시즌/이벤트, 대상/산업, 색상/무드를 우선 채운다.
- DesignHub 업로드 전에 reupload collision 가능성이 있으면 `../../scripts/prepare_designhub_unique_upload.py`로 업로드 안전 고유 basename을 준비한다.

## Validation

batch ready라고 말하기 전에 모두 확인한다.

- alpha channel이 존재한다.
- 투명 모서리가 통과한다.
- 체크보드, 흰색, 어두운 preview에서 visible key-color fringe가 없다.
- magenta-key run은 decontamination 뒤 남은 visible magenta-cast pixel이 `0`이다. 실제 magenta/purple 디테일을 보존해야 한다면 다른 key 또는 manual mask를 사용한다.
- key color와 비슷하다는 이유로 피사체 내부 디테일이 지워지지 않았다.
- 반투명 wind, breeze, air, mist, motion 효과가 key-color 오염 없이 보인다. 효과 보존을 위한 의도적인 outline/stroke는 허용한다.
- 확대 검수에서 edge가 계단형이 아니라 anti-aliased 상태다.
- 피사체가 잘리지 않았다.
- 각 최종 PNG는 자체 source asset 또는 full-resolution per-element source에서 왔고, cropped combined sheet에서 온 것이 아니다.
- 업로드용 PNG 요소를 요청받았다면 Photopea processed 출력이 존재한다.
- CSV basename이 최종 PNG basename과 일치한다.
- 사용자가 명시적으로 확인하지 않았다면 외부 DesignHub 업로드/제출은 수행하지 않았다.

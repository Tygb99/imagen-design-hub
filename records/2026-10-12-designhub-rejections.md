# DesignHub Rejections Read on 2026-10-12

[Korean](2026-10-12-designhub-rejections.ko.md)

The DesignHub rejected list showed 12 single elements, read without resubmitting on 2026-10-12 21:41–21:46 KST. The machine-readable list is [designhub-rejected-elements.csv](designhub-rejected-elements.csv); `scripts/designhub_preflight.py rejected` reads it before upload.

## Reason codes

- **A** (3 GIFs): uncropped transparent margin, plus 「품질 문제로 거부된 콘텐츠는 다시 제출할 수 없으며 해당 콘텐츠를 반복적으로 제출한 경우, 디자인허브 이용이 제한됩니다.」 Never resubmit.
- **B** (6 PNG elements): uncropped transparent margin; the artboard must fit the subject with no margin on any side.
- **C** (2 backgrounds): wrong content type; illustrations with a subject belong to an element type, not Background.
- **D** (1 PNG element): subject clipped or incomplete background removal.

## Columns

`no,elementName,fileName,contentType,submittedAt,rejectedAt,reasonCode`, copied from the DesignHub screen (times as shown there). Add new rejections as new rows with the same columns.

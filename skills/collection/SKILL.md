---
name: collection
description: Create and update MiriCanvas DesignHub collections from approved public PNG, SVG, or GIF elements. Check live limits and existing membership, group related elements, register names and keywords, and verify saved collection IDs and contents.
---

# Imagen Design Hub: Collections

[한국어](SKILL.ko.md)

Use for DesignHub collection limits, grouping approved elements, collection registration, or collection metadata edits. A request to add this capability to the plugin authorizes plugin changes; it does not request new live collections. For file upload, element CSV changes, or review submission, use [upload-csv](../upload-csv/SKILL.md) only when those actions are requested.

## Read current state

Use the installed Aside skill and current guide. Attach the matching existing tab, confirm the account, and inspect [collection management](https://designhub.miricanvas.com/ko/collection/manage) and [element management](https://designhub.miricanvas.com/ko/element/manage). Identify controls from fresh page evidence. Keep browser mutations in the UI; local tools may prepare manifests and compare downloaded CSVs.

- The management screen observed on 2026-10-21 allowed 400 collections and 30 elements per collection. Read the current limits before planning; these observations are not permanent constants.
- The list initially shows only recent registrations. Expand the date/search scope before claiming a total or calculating remaining capacity. A filtered count of zero does not prove there are no collections.
- Read the current [creation conditions](https://slashpage.com/designhub-guide/xjqy1g2vw99edm6vd54z): at least 6 public elements; one supported type per collection (PNG element, SVG element, or GIF); shared style/theme; each element belongs to only one collection. Collections have no separate review queue.
- Use live approval, visibility, and membership evidence. A historical CSV filename containing “approved” or “waiting” is not a current status check. Leave pending, review-waiting, rejected, private, and ineligible items out of the plan.

## Plan groups without duplicates

1. Resolve the intended batch from the conversation, local manifest, and live list. Keep unrelated account elements outside it. If the intended batch cannot be identified, ask for that missing scope before registration.
2. Build a stable mapping of source `fileName`, downloaded `uniqueId`, and the UI's numeric element ID. These are distinct identifiers. Preserve downloaded spellings; an optional extension may be normalized for matching only when the match is unique. Never resolve ambiguous names by list position.
3. Check existing collection membership for the target IDs across the relevant date range. Compare saved memberships, not just names or the latest 30 days. If a collection already has the intended ID set, verify and reuse it. Leave elements in other existing collections in place unless the user requests a move. If membership cannot be established, report the unresolved items instead of assuming they are free.
4. Partition eligible unassigned elements first by type, then by coherent subject/style. Inspect previews; identical keywords alone do not establish visual consistency. Keep each element in one planned group.
5. Respect the user's grouping within the live minimum and maximum. Otherwise choose `k = ceil(n / maximum)` and balance the elements across `k` groups, provided `n >= k * minimum`. With limits 6–30, 100 related elements can become four groups of 25; 31 can become 16 and 15. Do not leave a group of 1–5 or pad it with unrelated elements. Report any remainder that cannot form a valid collection.
6. Compare the required new groups with verified available collection slots. If capacity is insufficient, leave the excess planned and report it; do not hide or replace existing collections to free space.

Record the planned IDs before registration so an interrupted run can resume. An explicit request to create collections covers registration for that batch; do not ask for the same approval again. A limits-only question requires no registration.

## Names and keywords

Follow the user's requested language and naming rules. For Korean titles, use a short noun phrase in the order `색 + 스타일 + 모양 + 주제어 + 위치/역할` when those attributes describe the whole group. Use Korean color names, omit attributes that are not shared, and add a two-digit suffix only to distinguish related groups. Example: `분홍색 3D 아크릴 글자 블랙프라이데이 타이틀 01`.

Default to exactly 25 distinct Korean search terms, within the current UI limit; honor an explicit different count or language. Use shared subject/aliases first, subject-and-role combinations next, suitable use cases/seasons next, then style/material. Include a single representative color keyword in a different notation from the title, such as `분홍색` → `핑크`, only when one color represents the collection. Use an angle term only if it fits the group. Do not copy the union of all element keywords blindly. Omit standalone `아이콘`, `장식`, `데코`, `오브젝트`, file properties such as `PNG`/`투명배경`, production terms, and spelling errors. See [keyword guidance](../../references/keyword-generation.md) for additional search-term choices; these collection rules govern the default count.

## Register through Aside

1. In element management, select the group's exact items and check the selected count. Lists are virtualized: scroll an observed card into view, then read the newly rendered cards. Re-read after the first selection or a panel resize; columns and visible rows can change. DOM order is not a durable identity.
2. If a native checkbox is hidden under a visual card control, inspect the card DOM and target its own checkbox. Use `check({force:true})` only for the observed checkbox when normal checking cannot reach it. Resolve duplicate measurement cards by visibility or inspected DOM; `.last()` was appropriate in the observed UI, not a universal selector rule.
3. Open `컬렉션 만들기`, verify the type and element count, then `다음`. Compare the element IDs in the registration panel against the planned set before proceeding. Never paste CSV `uniqueId` values into the numeric element-ID field.
4. Fill the name and comma-separated keywords. The observed keyword control commits on a comma; filling text or pressing Enter alone did not commit it. If needed, move to the end and press comma, then verify the displayed keyword chips and count. Use the live control's name-length and keyword limits.
5. Capture the planned name, keywords, and IDs, then click `등록` once. Record the result. If it times out or is unclear, return to management and inspect the intended name/ID set before any retry. Resume only missing groups; after two unsuccessful retries on a confirmed absent group, report it and continue independent groups.
6. Reopen each saved collection. Confirm its assigned collection ID/key, exact name, keyword list/count, element ID set/count, and displayed status. A toast alone is not completion. If the card selects but the details remain closed, use the observed information-panel control. The observed UI supported clicking the card image; truncated title text was unreliable.

## Update existing collections

Resolve the collection by its assigned ID/key and reopen its details. Record its current membership, name, keywords, and visibility. Through `메타데이터 수정`, change only requested fields, save, and reopen to compare; preserve membership and visibility for a name/keyword-only request. Do not recreate a collection to edit its metadata.

The [management guide](https://slashpage.com/designhub-guide/3p4kj92ynppykm57q1x8) states that collections cannot be deleted; private/inactive states affect service visibility separately from element visibility. Apply visibility changes only when requested, and do not attempt to reactivate an administrator-disabled collection. If membership editing is unavailable in the current UI, report that limitation rather than creating a duplicate replacement.

## Evidence and handoff

Save UTF-8 CSV records in the current run, separate from element upload metadata:

- `collections.csv`: `collectionId,collectionKey,collectionName,contentType,elementCount,keywordCount,keywords,status,verifiedAt`
- `collection-members.csv`: `collectionId,fileName,uniqueId,elementId`

Keep planned groups in a separate local file until confirmed. Blank unknown IDs/statuses instead of inventing them. These are tracking files, not DesignHub upload templates. Preserve each identifier and put a timestamp on evidence snapshots; do not bundle private account records or login data into this plugin.

Compare planned and saved ID sets, check for duplicate element IDs across collections, and account for every intended item as registered, already assigned, ineligible, or unresolved. Report the verified collection and element counts, metadata state, and any remainder. Distinguish DesignHub registration/status from actual availability in the MiriCanvas editor; verify the latter separately only when requested. Leave the collection-management page open for the user.

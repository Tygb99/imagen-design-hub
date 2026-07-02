---
name: designhub-keyword-generation
description: Keyword generation reference for MiriCanvas and DesignHub element metadata.
---

# DesignHub Keyword Generation Reference

This guide distills the local research report `miricanvas_element_keyword_report (1).md` into reusable keyword-writing rules for DesignHub metadata. Treat it as a practical priority framework, not as an official ranking formula. MiriCanvas does not publish its internal search ranking weights.

## Core Principle

Write keywords for what buyers search for, not how the asset was produced.

Good keyword sets combine:

- subject or object
- element form
- style
- use case
- season or event
- audience or industry
- color or mood

The strongest formula is:

```text
subject/object + element form + style + use case + season/event + audience/industry + color/mood
```

## Count And Language

- Use 20 to 25 unique comma-separated keywords.
- Put the most concrete, official, and visually accurate terms first.
- Do not mix Korean and English in the same keyword list unless the user explicitly requests it.
- Treat 25 keywords as the current practical DesignHub/UI target, while rechecking the live UI if the policy appears to change.

## Priority Axes

Fill the list from these axes before adding loose synonyms:

| Axis | Question | Examples |
| --- | --- | --- |
| Subject/Object | What is it? | arrow, flower, hospital, coffee, dog, book, coupon |
| Element Form | What asset form is it? | icon, illustration, frame, sticker, pattern, chart |
| Style | How does it look? | hand-drawn, 3D, pixel, watercolor, minimal, vintage |
| Use Case | Where will it be used? | presentation, card news, poster, thumbnail, menu |
| Season/Event | When is it useful? | new year, spring, summer, Chuseok, Christmas |
| Audience/Industry | Who uses it? | school, clinic, cafe, church, shopping mall |
| Color/Mood | What feeling or palette? | blue, yellow, pastel, cute, clean, premium |

## Strong Demand Clusters

Prioritize clusters that match common template and element demand:

- documents and PPT: presentation, report, proposal, chart, graph, table
- social content: card news, Instagram, thumbnail, YouTube, profile
- promotion and commerce: event, sale, discount, coupon, banner, poster, detail page
- education: school, class, timetable, academy, teacher, student
- seasons: new year, spring, summer, Chuseok, CSAT, Christmas, year-end
- basic decoration: arrow, speech bubble, frame, icon, background, flower, heart, ribbon, star, check
- healthcare: hospital, medical, health, nurse, mask, medicine, consultation
- cafe and food: cafe, coffee, bread, dessert, menu, drink, recipe

## Avoid

Remove production, file, admin, and platform terms from `keywords` and `elementName`, including:

```text
Photopea, API, prompt, imagegen, background removal, PNG, JPG, SVG, GIF, MP4,
2D, 350DPI, transparent background, run IDs, dates, DesignHub, MiriCanvas,
CSV, Premium, clipart, design source, background source, decoration element
```

## Quality Check

Before accepting metadata:

- keyword count is 20 to 25
- every keyword is unique within the row
- top keywords describe the visible asset, not production steps
- subject/object, form, style, use case, and at least one demand signal are represented
- seasonal keywords match the asset and likely submission timing
- no unsupported claim is phrased as an official ranking factor

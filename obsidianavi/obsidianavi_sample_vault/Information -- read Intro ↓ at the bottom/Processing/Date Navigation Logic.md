---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Date Navigation Logic
Date: 2025-05-10
---
> [!navigation]+
> ⚓ Parent
> %%navi-p%%
> 
> 🔗 Siblings (%%navi-sc%%)
> %%navi-s%%
> 
> 🖇️ Children (%%navi-cc%%)
> %%navi-c%%

# Date Navigation Logic

## Summary
Explains how ObsidiaNavi creates links to Today, Yesterday, and Tomorrow based on a note’s date frontmatter.

## Details
If a note includes a frontmatter field defined in `date_settings.date_property_name` (e.g., `Date: 2025-05-10`), Navi:

- Parses it using `date_format`
- Generates adjacent dates by offsetting with ±1 day
- Converts each into a link (e.g., `[[2025-05-09|Yesterday]]`)

If the target date note isn’t present in the sibling list, Navi strikes through the alias (e.g., `~~Tomorrow~~`).

Aliases are configurable (e.g., `"yesterday": "A Day Ago"`) and substituted automatically into links:
- `%%​<navi-yest%%​[[2025-05-08|A Day Ago]]%%​navi-yest>%%​`
- `%%​navi-tod%%​[[2025-05-09|Today]]%%​navi-tod>%%​`
- `%%​navi-tom%%​[[2025-05-10|Tomorrow]]%%​navi-tom>%%​`

This logic allows seamless date-based navigation within daily notes.

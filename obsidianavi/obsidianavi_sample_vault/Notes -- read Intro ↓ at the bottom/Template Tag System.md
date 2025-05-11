---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Template Tag System
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

# Template Tag System

## Summary
Describes how ObsidiaNavi uses and transforms placeholder tags in notes to generate Obsidian links.

## Details
Navi uses a set of configurable template tags to mark insertion points for relationships and date-based links.

Examples include:
- `%%​navi-p%%​` → Parent links
- `%%​navi-s%%​` → Sibling links
- `%%​navi-c%%​` → Child links
- `%%​navi-pc%%​`, `%%​navi-sc%%​`, `%%​navi-cc%%​` → Link counts
- `%%​navi-tod%%​`, `%%​navi-yest%%​`, `%%​navi-tom%%​` → Relative dates

During processing:
1. Each plain tag is wrapped with a defined open/close marker (e.g., `%%​navi-p%%​`)
2. Navi replaces the wrapped tag with formatted Obsidian links or counts
3. The content can later be reverted to the original tag using `--revert`

This approach ensures tags are both configurable and reversible.


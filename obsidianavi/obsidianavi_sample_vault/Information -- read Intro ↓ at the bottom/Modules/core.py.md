---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: core
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

# Module: core

## Summary
Explains the orchestration logic found in the `core.py` module that drives vault processing.

## Details
The `core.py` file defines `process_vault()`, the main engine behind Navi's note transformation.

Responsibilities:
- Load markdown files using `list_markdown_notes`.
- Parse frontmatter into structured metadata.
- Filter files and folders via exclusion rules.
- Apply relationship detection (via `relat.py`) and sorting.
- Call `process_note_content()` or `revert_note_content()` for each note.
- Write changes to disk.

This module coordinates the note processing pipeline from loading to transformation to saving.

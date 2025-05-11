---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: process
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

# Module: process

## Summary
Covers ObsidiaNavi’s `process.py` module, which transforms note content based on relationships and date logic.

## Details
This module is responsible for editing note content:

- `process_note_content()`:
  - Replaces placeholder tags (e.g., `%%​navi-p%%​`) with wrapper tags for safe substitution.
  - Generates Obsidian links for parents, siblings, children.
  - Adds relative date links (Today, Yesterday, Tomorrow).
  - Replaces relationship counts.

- `revert_note_content()`:
  - Reverts modified tags back to their original placeholders.

It supports the full navigation rendering lifecycle and ensures that output is readable, reversible, and conforms to configuration rules.


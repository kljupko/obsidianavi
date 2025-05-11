---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: relat
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

# Module: relat

## Summary
Details the logic in `relat.py`, the module responsible for inferring relationships between notes.

## Details
The `relat` module defines how Navi determines which notes are:

- **Parents**: Notes with one fewer hierarchy key and a matching shared key path.
- **Siblings**: Same depth and shared parent key values.
- **Children**: Notes with one more hierarchy key and matching all current keys.

Functions include:
- `find_parents()`
- `find_siblings()`
- `find_children()`
- `get_note_relationships()` — aggregates all three into a single metadata object.

It relies on strict comparison of YAML frontmatter key-value pairs using the configured `hierarchy_keys`.

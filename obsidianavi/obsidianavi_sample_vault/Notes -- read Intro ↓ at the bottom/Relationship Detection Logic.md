---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Relationship Detection Logic
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

# Relationship Detection Logic

## Summary
Describes how ObsidiaNavi uses frontmatter metadata to infer parent, sibling, and child note relationships.

## Details
Navi compares frontmatter keys (from `hierarchy_keys`) across notes to establish relationships:

- **Parents**:
  - One level up (fewer keys)
  - Shared metadata for all keys present in the parent
- **Siblings**:
  - Same number of keys
  - Shared values for all keys except the last
- **Children**:
  - One more key
  - All current keys and values must match

This logic is implemented in `relat.py` via:
- `find_parents()`
- `find_siblings()`
- `find_children()`

It is sensitive to ordering and consistency of keys in the configuration.

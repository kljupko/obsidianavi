---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Basic Concepts
Topic: Note Relationships
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

# Note Relationships

## Summary
Explains how ObsidiaNavi identifies and links notes through parent, sibling, and child relationships based on metadata.

## Details
Navi determines relationships between notes using the configured frontmatter keys (e.g., `Function`, `Domain`, `Sub-domain`), forming an implicit hierarchy.

- **Parents**: Notes with one fewer hierarchy key and matching values up to that level.
- **Siblings**: Notes at the same hierarchy depth that share all parent keys.
- **Children**: Notes with one additional hierarchy key, whose parent keys match the current note.

These relationships are embedded using placeholder tags (e.g., `%%​navi-p%%​`, `%%​navi-s%%​`, `%%​navi-c%%​`) which Navi replaces with formatted Obsidian links during processing.

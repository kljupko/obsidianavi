---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Note Hierarchy Detection
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

# Note Hierarchy Detection

## Summary
Explains how ObsidiaNavi determines the hierarchical level of each note based on its frontmatter.

## Details
Each note’s hierarchy is inferred from the presence and order of configured `hierarchy_keys` in its frontmatter.

Steps:
1. Navi reads the frontmatter for each `.md` file.
2. It checks which keys from the `hierarchy_keys` list are present (e.g., `Subject`, `Area`, `Topic`).
3. The number of matched keys determines the note’s level (e.g., 3 keys = level 3).

This level influences:
- Which notes are considered parents (one level up)
- Which are siblings (same level, shared parents)
- Which are children (one level down, extended key path)

The more keys a note includes from the configured list, the deeper it is in the conceptual hierarchy Navi uses to link notes together.

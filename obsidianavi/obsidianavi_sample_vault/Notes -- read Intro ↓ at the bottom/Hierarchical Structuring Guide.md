---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Metadata & Frontmatter Usage
Topic: Hierarchical Structuring Guide
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

# Hierarchical Structuring Guide

## Summary
How the order and presence of keys shape the navigation graph.

## Details

Navi builds relationships between notes based on **how many hierarchy keys** they contain and how many match.

The general rules are:

- **Parents**: One fewer key, all matching values
- **Siblings**: Same number of keys, all parent keys match
- **Children**: One more key, all parent keys match

### Example:
```yaml
Note A:
Function: Tutorial
Domain: Technology

Note B:
Function: Tutorial
Domain: Technology
Sub-domain: Computer Science
```

- Note A is the **parent** of Note B
- Note B is a **child** of Note A
- Any other notes with the same Function and Topic are **siblings**

The structure is flexible and driven by metadata — not folders, filenames, or note links.

---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Basic Concepts
Topic: Frontmatter Metadata Model
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

# Frontmatter Metadata Model

## Summary
Describes how ObsidiaNavi uses frontmatter to extract structure and relationships from markdown notes.

## Details
Navi expects notes to include YAML frontmatter with flat key-value pairs. It uses configured `hierarchy_keys` (from `obsidianavi_config.json`) to establish structural levels.

Example frontmatter:
```yaml
---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
---
```

The number and order of these keys determine the note's level in the hierarchy. This model allows Navi to compare notes and infer relative positions — essential for establishing parent, sibling, and child links.

Date-based behavior uses a separate field (default: `Date`) and can be customized via `date_settings`.

```yaml
---
Function: Journal
Date: 2025-05-15
---
```
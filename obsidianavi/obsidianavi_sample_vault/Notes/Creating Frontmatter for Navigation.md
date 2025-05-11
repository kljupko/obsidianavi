---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Metadata & Frontmatter Usage
Topic: Creating Frontmatter for Navigation
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

# Summary
How to use frontmatter keys to participate in ObsidiaNavi's logic.

## Details

Frontmatter is the heart of how Navi works.

Each note must begin with a block like this (by default):

```yaml
---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Using Navi
Topic: Writing Links with Navi
---
```

This tells Navi where the note belongs in a hierarchy — and that’s how it decides what’s a parent, child, or sibling.

The required fields are defined in the `hierarchy_keys` config. By default, they are:

```json
["Function", "Domain", "Sub-domain", "Subject", "Area", "Topic", "Aspect", "Detail", "Facet"]
```

Your notes don’t need to have *all* of these — just enough to define their place relative to others. But they **should** be in the same order as in the config.

Once you’ve added metadata, Navi will be able to link your notes automatically.

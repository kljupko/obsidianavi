---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Getting Started
Topic: Vault Structure
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

# Vault Structure

## Summary
How to organize your vault so ObsidiaNavi can process it properly.

## Details

This vault is already structured in a way that works with Navi — and understanding why helps you use Navi confidently on your own notes later.

Here’s what matters:

- Each note contains a **frontmatter block** at the top — that’s the YAML section wrapped in `---` (in Source mode).
- Navi looks for specific metadata fields like `Function`, `Domain`, `Sub-domain`, etc., and later you can even learn how to set up your own fields if these don't work for you.
- These fields form a **hierarchical structure** that Navi uses to detect relationships:
  - Notes with the same parent are *siblings*
  - Notes with more or fewer levels of metadata become *children* or *parents*

Navi doesn't care about:
- What folder the note is in
- The filename or title

In fact, **all of the notes in this vault will be processed as if they’re in one big flat list**, sorted and linked purely by metadata.

Once you understand that, you’re ready to actually run Navi and see it work.

> Head to step 3/3: **[[Running Navi for the First Time]]** to generate your first set of links.


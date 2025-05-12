---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Using Navi
Topic: Generating Links with Navi
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

# Generating Links with Navi

## Summary
How to run `--write` and what it updates.

## Details

This is the most common command you’ll use with Navi (assuming you don't automate it):

```bash
obsidianavi --write
```

It tells Navi to scan all notes, identify relationships, and replace placeholder tags with formatted Obsidian links.

You can run it multiple times — it won’t duplicate content or overwrite anything important. It simply checks your frontmatter and regenerates the navigation blocks.

If you add new notes later or change metadata, just run `--write` again to refresh the links.

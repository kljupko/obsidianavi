---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Using Navi
Topic: Processing Specific Notes Only
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

# Processing Specific Notes Only

## Summary
Restrict ObsidiaNavi's scope with the `--notes` flag.

## Details

Sometimes, you may only want to update a few notes — not the whole vault.

You can use the `--notes` option to specify one or more note names:

```bash
obsidianavi --write --notes "Note A" "Note B"
```

This will:
- Only process those files (provided they are not excluded in the config)
- Still honor the config and frontmatter relationships
- Not touch any other notes in your vault

You can combine this with `--revert` too:

```bash
obsidianavi --revert --notes "Note A"
```

This is helpful for testing changes or focusing on a specific topic.

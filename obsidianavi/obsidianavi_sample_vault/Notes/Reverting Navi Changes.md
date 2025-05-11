---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Using Navi
Topic: Reverting Navi Changes
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

# Reverting Navi Changes

## Summary
Undo ObsidiaNavi output using `--revert`.

## Details

If you want to undo the changes made by Navi, just run:

```bash
python -m obsidianavi.cli --revert
```

This will:
- Remove all links added by Navi
- Restore the original placeholder tags (`%%​navi-p%%​`, etc.)

This is safe and non-destructive. Navi only touches content it created — nothing else is altered or deleted.

You can run `--revert` at any time, then run `--write` again if needed.

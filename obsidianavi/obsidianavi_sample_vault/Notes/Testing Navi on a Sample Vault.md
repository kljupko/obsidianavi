---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Using Navi
Topic: Testing Navi on a Sample Vault
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

# Testing Navi on a Sample Vault

## Summary
Test ObsidiaNavi on a dummy vault and observe relationships.

## Details

Before using Navi on your personal notes, you can try it out on this vault as a test environment.

This vault was designed to demonstrate:
- Hierarchical relationships
- Date-based linking
- Custom template tags
- Configurable exclusions

To see it in action:
1. Open this vault in Obsidian
2. Run:
   ```bash
   obsidianavi --write
   ```
3. Click around — look for the `[!navigation]` blocks and follow the links

You can revert everything cleanly at any time:

```bash
obsidianavi --revert
```

Experiment freely. That’s what this vault is for.
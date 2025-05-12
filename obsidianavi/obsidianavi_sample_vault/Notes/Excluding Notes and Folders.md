---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Configuration Tutorials
Topic: Excluding Notes and Folders
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

# Excluding Notes and Folders

## Summary
Guide to setting up exclusions for files and folders.

## Details

You can tell Navi to skip certain notes or folders entirely during processing.

This is helpful for:
- Templates
- Archive folders
- Notes without meaningful metadata

To exclude items, edit the config file or use the CLI.

**Examples** (CLI):
```bash
obsidianavi --add exclude_files=README
obsidianavi --add exclude_folders=Templates
```

You can check what's currently excluded by running:

```bash
obsidianavi --show-config
```

Matching is done by substring — if the file or folder name contains the value you provide, it will be ignored.

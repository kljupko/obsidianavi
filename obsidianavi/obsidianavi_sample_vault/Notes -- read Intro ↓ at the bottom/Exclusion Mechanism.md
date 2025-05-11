---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Exclusion Mechanism
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

# Exclusion Mechanism

## Summary
Describes how ObsidiaNavi excludes specific files or folders from processing based on the configuration.

## Details
The config file supports two lists for exclusions:

- `"exclude_files"`: substring match against filenames (e.g., `"README"`)
- `"exclude_folders"`: substring match against folder paths (e.g., `"Templates"`)

These lists are applied during `process_vault()`:
- Notes whose filenames contain a listed string are skipped
- Notes in folders (or subfolders) containing listed strings are also skipped

Matching is substring-based and may behave differently on case-sensitive vs. insensitive systems. This mechanism ensures Navi does not modify notes in templates, trash, or non-content folders.

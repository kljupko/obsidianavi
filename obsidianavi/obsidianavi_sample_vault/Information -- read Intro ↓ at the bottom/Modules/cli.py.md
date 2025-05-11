---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: cli
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

# Module: cli

## Summary
Explains the purpose and logic of the `cli.py` module, ObsidiaNavi's main entry point.

## Details
The `cli.py` module is invoked via `python -m obsidianavi.cli` and serves as the command-line interface to the tool. It:

- Parses CLI arguments using `parse_args()`.
- Loads configuration via `ConfigManager`.
- Handles flag logic (e.g., `--write`, `--revert`, `--show-config`).
- Invokes `process_vault()` to generate or revert navigation links.
- Saves updated config when using `--set`, `--add`, or `--remove`.

This module enables all user interaction and determines which backend processes to execute.

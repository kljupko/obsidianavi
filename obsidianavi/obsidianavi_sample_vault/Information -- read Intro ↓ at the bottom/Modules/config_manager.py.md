---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: config_manager
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

# Module: config_manager

## Summary
Documents the logic behind ObsidiaNavi’s configuration handling system in `config_manager.py`.

## Details
This module defines the `ConfigManager` class, which handles reading, modifying, saving, and resetting the user configuration JSON file at `~/.config/obsidianavi/obsidianavi_config.json`.

Key responsibilities:
- Load and save configuration safely.
- Apply changes via `--set`, `--add`, and `--remove` CLI options.
- Support dot-path navigation for nested keys.
- Reset user config using the default `obsidianavi_config.json`.

It ensures that configuration changes are validated and persisted with appropriate feedback.

> [!warning]
> Modifying the configuration file manually risks breaking the app (trailing commas, or similar issues). Therefore, you should only use the CLI to modify the configuration.

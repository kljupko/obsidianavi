---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
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

# Architecture: Modules

## Summary
Outlines the main Python modules that compose ObsidiaNavi and how responsibilities are divided among them.

## Details
Navi follows a modular design to isolate different concerns:

- `cli.py`: Entry point, handles CLI flags and dispatch logic.
- `arg_parser.py`: Parses command-line arguments into structured objects.
- `config_manager.py`: Loads, modifies, and saves the JSON configuration.
- `core.py`: Coordinates vault processing, exclusion logic, and I/O flow.
- `relat.py`: Contains logic for determining note relationships (parents/siblings/children).
- `process.py`: Performs tag substitution and content transformation.
- `io.py`: Handles reading/writing files and extracting frontmatter.

This division allows for clean separation between input handling, config management, relationship logic, and note transformation.

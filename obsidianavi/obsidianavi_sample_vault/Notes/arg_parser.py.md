---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: arg_parser
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

# Module: arg_parser

## Summary
Describes the `arg_parser` module, which interprets CLI arguments passed to ObsidiaNavi.

## Details
The `arg_parser.py` file defines a `CLIArgs` dataclass to hold all possible command-line options, and a `parse_args` function to populate it.

Handled flags include:
- `--write`, `--revert`: Control content transformation.
- `--notes`: Restrict operation to specific files.
- `--set`, `--add`, `--remove`: Modify config dynamically.
- `--show-config`, `--reset`, `--get`: Config management.

It provides structured, type-safe parsing and ensures other components receive validated input.

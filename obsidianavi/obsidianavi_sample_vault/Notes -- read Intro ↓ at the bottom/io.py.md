---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Modules
Topic: io
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

# Module: io

## Summary
Describes ObsidiaNavi's I/O logic for reading and writing markdown notes and extracting frontmatter.

## Details
The `io.py` module abstracts filesystem operations and metadata parsing. It includes:

- `list_markdown_notes()`: Recursively finds `.md` files in the vault.
- `extract_frontmatter()`: Reads and parses YAML-style frontmatter.
- `parse_note_metadata()`: Converts markdown notes into structured metadata used for relationships.
- `read_note()` and `write_note()`: Low-level functions for file I/O.

This module isolates all filesystem operations, allowing higher-level logic to work with clean abstractions.

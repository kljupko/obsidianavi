---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Navigation Callout Styling
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

# Navigation Callout Styling

## Summary
Explains how ObsidiaNavi styles its output using a `[!navigation]` callout and related formatting options.

## Details
You may use a `[!navigation]` callout block to visually group inserted links in the processed note. This callout may include:

- **Parent**, **Sibling**, and **Child** sections
- Optional counts (e.g., `%%​navi-pc%%​`)
- Configurable markers in `obsidianavi_config.json` for opening and closing each section

Additional styling behavior is controlled via the `obsidianavi_callout` config:
- `separator`: string between links
- `use_nonbreaking_space`: replaces spaces for visual alignment
- `is_self_italic` / `is_self_linked`: controls formatting for the current note

These settings make Navi’s output readable and visually consistent within Obsidian.

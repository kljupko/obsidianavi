---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
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

# Processing: Content Transformation

## Summary
Describes how ObsidiaNavi processes note content by replacing tags and inserting navigation links.

## Details
These notes explain Navi’s rendering pipeline — how it converts raw notes with placeholders into rich, linked documents:

- **Tag Replacement**: Wraps and substitutes template tags (e.g., `%%​navi-p%%​`) with formatted Obsidian links.
- **Callout Styling**: Groups relationships into a collapsible `[!navigation]` block.
- **Date Navigation**: Inserts links to Yesterday, Today, and Tomorrow notes based on a frontmatter date.
- **Self-Sibling and Filtering**: Handles edge cases like including the current note and skipping excluded files or folders.

This collection details the transformation logic that makes the final output usable inside Obsidian.

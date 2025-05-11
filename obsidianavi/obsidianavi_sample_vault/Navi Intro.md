---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
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

# Navi Overview

## Summary
This note introduces ObsidiaNavi (or just "Navi" for short) — a command-line tool for enriching Obsidian notes with metadata-driven navigation links.

## Details
Navi is a lightweight Python utility that scans your Obsidian vault and adds contextual links between notes based on their YAML frontmatter metadata. It automatically detects hierarchical relationships (parents, siblings, children) and date-based links (Today, Yesterday, Tomorrow), enhancing navigation without requiring Obsidian plugins.

Core design principles include:
- **Non-intrusiveness**: Changes are reversible.
- **Configurability**: Controlled via a JSON config file.
- **Portability**: Pure Python with minimal dependencies.

The tool supports batch processing, selective note targeting, and metadata-driven structure inference.

## Additional Information
To get used to the hierarchical structure of Navi, almost no links were provided in these notes, even though a real note would contain them. Furthermore, the information notes are not distributed across folders. If you wish to learn more about Navi, you will need to generate the links for this vault via the CLI.

To get started on that, click this [[Tutorial]] link, and you will be guided through the process.
# ObsidiaNavi — Metadata-Driven Navigation for Obsidian Notes

![navi](https://github.com/user-attachments/assets/910b1e47-a4f5-4892-aa9b-5d163e35a15a)



ObsidiaNavi (or "Navi" for short) is a command-line tool that automatically links your Obsidian markdown notes using structured frontmatter metadata. It turns your vault into a navigable, wiki-style knowledge system — powered entirely by fields you define.

* 🧠 Understand your note relationships: **parents**, **siblings**, **children**
* 🗓 Link across **daily notes** like "Today", "Yesterday", "Tomorrow"
* 🎯 Process all notes or **target specific ones**
* ↺ Fully **reversible** output with a single command
* 💾 Includes a **sample vault** wiki for the tool and a CSS snippet for styling

---

## ⚠️ Disclaimer

**This tool is still experimental and actively being tested.**

By using ObsidiaNavi, you acknowledge that:

* You are solely responsible for the safety of your files and data.
* The author of this tool is **not liable for any loss, corruption, or unintended changes** to your notes.
* You should always **make a complete backup of your data** before using Navi.

Use at your own risk.

---

## 📦 Installation

To install Navi using pip from the GitHub repository:

```bash
pip install git+https://github.com/kljupko/obsidianavi.git
```

Then initialize it:

```bash
obsidianavi
```

This sets up:

* A config file in `~/.config/obsidianavi/obsidianavi_config.json` (or equivalent for MacOS or Windows)
* A sample vault in your `~/Documents/` directory

---

## 🚀 Basic Usage

After initializing Navi, you may use the tutorial in the sample vault in your `/Documents` folder to learn everything you need to know about Navi.
Below is a quick demonstration og how you may use Navi.

### Generate navigation links in your notes:

```bash
obsidianavi --write
```

This scans your configured vault (sample vault by default), analyzes frontmatter metadata, and replaces template tags like `%%navi-p%%` with real Obsidian links for parents, siblings, and children.

### Undo the changes:

```bash
obsidianavi --revert
```

This safely reverts only what Navi changed — returning your notes to their placeholder tag state.

### Limit scope to specific notes:

```bash
obsidianavi --write --notes "Note A" "Note B"
```

You can also use this with `--revert` to selectively undo.

---

## 🧪 Try It First (Recommended)

Before linking your personal notes, test Navi on the included **sample vault**:

```bash
obsidianavi --write
```

Then explore the generated links and navigation blocks inside Obsidian.

If you want to reset the vault or config:

```bash
obsidianavi --reset
```

---

## ⚙️ Configuration

The config file controls:

* What folders/files to exclude
* How metadata is interpreted (`hierarchy_keys`)
* Template tags used for substitution
* Behavior for date-based notes
* Output formatting

You can edit it using the CLI:

```bash
# View full config
obsidianavi --show-config

# Set a new vault path
obsidianavi --set vault_directory=~/Documents/my_real_vault

# Add a hierarchy key
obsidianavi --add hierarchy_keys=Facet

# Remove an excluded folder
obsidianavi --remove exclude_folders=Templates
```

---

## 📁 Metadata Model (How It Works)

Navi determines relationships using frontmatter keys:

```yaml
---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Topic: Configuration
---
```

* Notes with **one fewer key** are considered **parents**
* Notes with **matching parent keys** are **siblings**
* Notes with **one additional key** are **children**

> You don’t need to use all keys — just be consistent and in order.

The default hierarchy:

```json
["Function", "Domain", "Sub-domain", "Subject", "Area", "Topic", "Aspect", "Detail", "Facet"]
```

---

## 🗓 Date-Based Linking

If your notes have a date like:

```yaml
Date: 2025-05-10
```

Navi can generate links like:

```
[[2025-05-09|Yesterday]]
[[2025-05-10|Today]]
[[2025-05-11|Tomorrow]]
```

Missing notes will be shown with strikethroughs. You can configure aliases and formats via the `date_settings` config section.

---

## 🎨 Styling with Obsidian

To highlight Navi’s output, use the included CSS snippet.
Steps:

1. Copy `obsidianavi-callout.css` from the sample vault
2. Place it in your Obsidian snippets folder
3. Enable it in **Settings → Appearance → CSS Snippets**

You may need to quit and re-enter Obsidian for the navigation icon to render correctly.

---

## 🧰 Template Tags

Your notes should contain Navi placeholder tags where links should appear:

```markdown
%%navi-p%%     → Parents
%%navi-s%%     → Siblings
%%navi-c%%     → Children
%%navi-pc%%    → Parent count (sc and cc for Siblings and Children)
%%navi-yest%%  → Yesterday (tod and tom for Today and Tomorrow)
```

These are replaced during `--write` and restored during `--revert`. You can customize tag names in your config.

---

## 🧠 Example Workflow

```bash
# Install
pip install git+https://github.com/kljupko/obsidianavi.git

# Initialize config and sample vault
obsidianavi

# Explore sample vault in Obsidian

# Generate links
obsidianavi --write

# Revert if needed
obsidianavi --revert

# Target your own vault
obsidianavi --set vault_directory=~/Documents/my_notes

# Process your own notes
obsidianavi --write
```

---

## 🛠 Developer Notes

Navi is modular and built with clean separation of logic:

* `cli.py`: Command-line interface
* `core.py`: Vault scanning and orchestration
* `relat.py`: Relationship inference
* `process.py`: Tag substitution and formatting
* `config_manager.py`: Config loading and CLI edits
* `io.py`: Frontmatter parsing and file I/O

The sample vault also includes documentation notes mirroring the codebase — ideal for onboarding new users or contributors.

---

## 📌 Caveats & Recommendations

* Always **back up your vault** before first use
* Navi only touches lines containing its configured tags
* Exclusions are matched by **substring**, not full paths
* Tags are reversible — experimentation is encouraged!

---

## 🧽 Credits

Created by [Ljupko Kolak](https://github.com/kljupko)

Tested on Linux & Windows.
Contributions welcome via GitHub.

---

## 📜 License

MIT


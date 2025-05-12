---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Configuration Tutorials
Topic: Understanding the Config File
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

# Understanding the Config File

## Summary
Understand `navi_config.json`, its location, structure, and what each setting controls.

## Details

When you run Navi for the first time, it creates a configuration file inside a hidden folder in your system. For Linux, that is at:

```
~/.config/obsidianavi/obsidianavi_config.json
```

This file tells Navi how to behave — what to scan, what to ignore, what metadata to use, and how to format its output.

You can edit it manually (assuming you can find it), or use CLI options to update it safely. Here’s what each section means:

---

### 🔁 `vault_directory`

```json
"vault_directory": "."
```

Specifies the folder Navi will treat as your vault root.  
- `"."` means "wherever the command was run from"
- You can set this to an absolute or relative path
If you have a personal vault in your `/Documents` folder, you can set it up to be something similar to this (assuming Linux):

```bash
obsidianavi --set vault_directory='/home/username/Documents/name_of_your_vault'
```

> [!caution]
> Remember to **back up your vault beforehand**, as this tool is still being tested.

---

### 🧼 `exclude_files` and `exclude_folders`

These let you skip specific files or folders during processing:

```json
"exclude_files": ["README", "Example"]
"exclude_folders": [".obsidian", "Templates"]
```

- Matching is case-sensitive and based on **substring** — so `"README"` would skip `README.md`, `project_README_notes.md`, etc.
- Useful for ignoring scratch files, template folders, system directories, etc.

---

### 🗂 `hierarchy_keys`

```json
"hierarchy_keys": ["Function", "Domain", "Sub-domain", "Subject", "Topic", "Aspect", "Detail", "Facet"]
```

These keys define the **metadata structure** Navi uses to infer relationships between notes. Each key represents one “layer” in a hierarchy.

- Notes with more keys are **children** of those with fewer keys (if values match up)
- Notes with the same key depth and shared parent values are **siblings**

> [!tip]
> You don’t need to use all keys — just be consistent.
---

### 📅 `date_settings`

```json
"date_settings": {
  "date_property_name": "Date",
  "date_format": "%Y-%m-%d",
  "aliases": {
    "yesterday": "Yesterday",
    "today": "Today",
    "tomorrow": "Tomorrow"
  }
}
```

Controls how Navi generates links for Today, Yesterday, and Tomorrow using the date in a note’s frontmatter.

- `date_property_name` is the frontmatter key to look for (usually `"Date"`)
- `date_format` must match the format used in your notes
- `aliases` define the visible text that will be used for the links

Example:
If a note has `Date: 2025-05-10`, Navi will generate:

```
[[2025-05-09|Yesterday]]
[[2025-05-10|Today]]
[[2025-05-11|Tomorrow]]
```

If no matching note is found, the alias will be struck through.

---

### 🧩 `template_tags`

```json
"template_tags": {
  "parents": "%%​navi-p%%​",
  "siblings": "%%​navi-s%%​",
  "children": "%%​navi-c%%​",
  "parent_count": "%%​navi-pc%%​",
  "sibling_count": "%%​navi-sc%%​",
  "child_count": "%%​navi-cc%%​",
  "yesterday": "%%​navi-yest%%​",
  "today": "%%​navi-tod%%​",
  "tomorrow": "%%​navi-tom%%​"
}
```

These are the placeholder tags Navi looks for inside your notes. When you run `--write`, Navi replaces these with actual links.

- You can customize the tags if they conflict with other tools
- Only the tags included in the config will be processed

---

### 🧱 `tag_wrappers`

```json
"tag_wrappers": {
  "open_...": "%%​<...",
  "close_...": "...>%%​"
}
```

These define how Navi wraps tags before substitution.

For example, `%%​navi-s%%​` becomes `%%​<navi-s%%​navi-s%%​%%​navi-s>%%​` internally before being replaced by `%%​<navi-s%%​[sibling ]/[sibling2]/...`

Unless you're doing something advanced, you don’t need to change these.

---

### 🧭 `navi_link`

```json
"navi_link": {
  "separator": "/",
  "use_nonbreaking_space": true,
  "is_self_sibling": true,
  "is_self_italic": true,
  "is_self_linked": false
}
```

Controls how Navi treats the **current note** when it's in its own sibling list, as well as how links are displayed

- `separator`: how links are separated (`" "` for space, `" • "` for bullets, etc.)
- `use_nonbreaking_space`: helps prevent line wrapping in links
- `is_self_sibling`: include the current note?
- `is_self_italic`: format the current note in italics?
- `is_self_linked`: should the current note link to itself?

These are mostly stylistic — use them to match your vault’s tone.

---

You can safely change any of these settings using:
- `--set key=value`
- `--add key=value` (for lists)
- `--remove key=value`

See [[Editing Config via CLI]] for examples.

---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Configuration Tutorials
Topic: Editing Config via CLI
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

# Summary
Use `--set`, `--add`, and `--remove` to update ObsidiaNavi’s config directly from the terminal.

## Details

Instead of editing `obsidianavi_config.json` by hand, you can safely update settings using the CLI. Changes are saved immediately.

---

### 🧠 Command Types

#### 1. `--set` — Update scalar values (e.g. strings, booleans)

```bash
python -m obsidianavi.cli --set vault_directory=./vaults/notes
```

#### 2. `--add` — Add to list-type values (e.g. folders, tags)

```bash
python -m obsidianavi.cli --add exclude_files=README
python -m obsidianavi.cli --add hierarchy_keys=Area
```

#### 3. `--remove` — Remove from lists

```bash
python -m obsidianavi.cli --remove exclude_folders=Trash
```

> ✅ These commands use **dot notation** to access nested values:
> - `obsidianavi_link.is_self_sibling=true`
> - `date_settings.date_format=%Y-%m-%d`

---

### 📋 Examples

#### Change the date format
```bash
python -m obsidianavi.cli --set date_settings.date_format=%Y/%m/%d
```

#### Add a custom hierarchy key
```bash
python -m obsidianavi.cli --add hierarchy_keys=Facet
```

#### Remove a file exclusion
```bash
python -m obsidianavi.cli --remove exclude_files=README
```

---

### 🔍 Check your config

Use this to preview your current config as formatted JSON:

```bash
python -m obsidianavi.cli --show-config
```

Or retrieve a single value:

```bash
python -m obsidianavi.cli --get template_tags.parents
```

---

This CLI-based editing is especially useful when scripting, version-controlling config, or automating updates across teams or vaults.

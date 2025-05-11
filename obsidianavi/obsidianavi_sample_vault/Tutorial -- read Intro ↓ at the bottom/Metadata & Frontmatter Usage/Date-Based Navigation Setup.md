---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Metadata & Frontmatter Usage
Topic: Date-Based Navigation Setup
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

# Date-Based Navigation Setup

## Summary
Use date metadata and test date-relative links.

## Details

Navi can create links to **Today**, **Yesterday**, and **Tomorrow** — but only if your notes include a date field in the frontmatter.

### Step 1: Add a date to your notes
```yaml
Date: 2025-05-10
```

This must match the format defined in your config (default is `YYYY-MM-DD`).

### Step 2: Include the date tags
Add these tags to any note:

```
%%​navi-yest%%​  → Yesterday
%%​navi-tod%%​   → Today
%%​navi-tom%%​   → Tomorrow
```

Navi will replace them with real links, like:

```
[[2025-05-09|Yesterday]]
[[2025-05-10|Today]]
[[2025-05-11|Tomorrow]]
```

If a note for that date doesn’t exist, Navi will strike through the alias to show it’s missing.

You can customize aliases and formats in the `date_settings` section of your config.

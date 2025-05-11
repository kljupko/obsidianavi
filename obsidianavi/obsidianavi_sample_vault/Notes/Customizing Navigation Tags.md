---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Configuration Tutorials
Topic: Customizing Navigation Tags
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

# Customizing Navigation Tags

## Summary
Modify `template_tags` to control where and how links appear.

## Details

Navi looks for special placeholder tags like `%%​navi-p%%​`, `%%​navi-s%%​`, and `%%​navi-c%%​` to know where to insert links.

These are defined in your config under the `template_tags` section.

You can change:
- Which tags trigger link placement
- Whether Navi generates counts (e.g. `%%​navi-pc%%​`)
- Which tags apply to dates (`%%​navi-yest%%​`, etc.)

**Example** config snippet:
```json
"template_tags": {
  "parents": "%%​navi-p%%​",
  "siblings": "%%​navi-s%%​",
  "children": "%%​navi-c%%​"
}
```

You can also adjust how tags are wrapped (start and end markers), or just remove a tag if you don’t want to use it at all.

> [!tip]
> Don’t include angle brackets or wrap tags yourself. Navi handles that automatically.

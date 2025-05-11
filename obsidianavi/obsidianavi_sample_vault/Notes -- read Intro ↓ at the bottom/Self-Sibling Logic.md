---
Function: Information
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Processing
Topic: Self-Sibling Logic
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

# Self-Sibling Logic

## Summary
Explains ObsidiaNavi’s behavior for including the current note as part of its own sibling list.

## Details
Navi supports an optional configuration setting:  
`navi_callout.is_self_sibling = "true"`

When enabled:
- The current note appears in its own sibling section
- Its name is formatted according to:
  - `is_self_italic`: render as *italic*
  - `is_self_linked`: render as `[[linked]]` or plain text

This is useful for consistent alignment or callout aesthetics when siblings are always expected in context, including the current note.

If disabled, the current note is excluded from its sibling group entirely.

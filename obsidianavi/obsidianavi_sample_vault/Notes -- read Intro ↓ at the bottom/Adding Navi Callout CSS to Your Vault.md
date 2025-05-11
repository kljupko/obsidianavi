---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Configuration Tutorials
Topic: Adding Navi Callout CSS to Your Vault
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

# Adding Navi Callout CSS to Your Vault

## Summary
Use a custom CSS snippet to style ObsidiaNavi’s `[!navigation]` blocks inside Obsidian.

## Details

You can place the links you want Navi to generate inside a `[!navigation]` callout block — which Obsidian can style with CSS. To help you make it stand out, a ready-to-use CSS snippet is included in this package.

You’ll find it in the package folder after installing or downloading the repo:

```
/css/obsidianavi-callout.css
```

### 💡 How to use it in Obsidian

1. Open Obsidian and go to:  
   **Settings → Appearance → CSS Snippets**

2. Click **“Open snippets folder”**

3. Copy the file `obsidianavi-callout.css` into that folder

4. Go back to Obsidian and enable the snippet

> That’s it — Navi’s `[!navigation]` blocks will now use the custom color and icon, and you can even style it as you see fit!

---

### Example Styling

```css
.callout[data-callout="navigation"] {
  --callout-color: 90, 100, 255;
  --callout-icon: lucide-compass;
}
```

This snippet:
- Sets a unique color for the block
- Adds the compass-style navigation icon
- Keeps your visual hierarchy easy to scan

You can tweak the snippet to match your own theme, or copy it into a larger vault-wide snippet if you prefer.

---

This is purely cosmetic — but it makes using Navi feel a lot smoother in practice.

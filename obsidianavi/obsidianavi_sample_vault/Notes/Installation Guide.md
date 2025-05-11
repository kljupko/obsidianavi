---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Getting Started
Topic: Installation Guide
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

# Installation Guide

## Summary
How to install ObsidiaNavi, create the virtual environment, and install dependencies.

## Details

If you’ve opened this vault, Navi is probably already installed — but if you ever need to re-install or set it up on a different machine, here’s how:

### 1. Clone the repository (or download the code)
```bash
git clone https://github.com/kljupko/obsidianavi.git
cd obsidianavi
```

Or download the `.zip` from GitHub and extract it.

### 2. (Optional) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install the package
```bash
pip install .
```

Navi is now ready to use. You can test it with:

```bash
python -m obsidianavi.cli --show-config
```

You should see the current configuration printed to the terminal.

> You only need to do this once per machine. After that, you can run Navi from anywhere.

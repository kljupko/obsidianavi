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

### 1. Install it with `pip`

Use `pip` to install the package directly from github. Open your terminal and enter the following (requires `pip`):

```bash
pip install git+https://github.com/kljupko/obsidianavi.git
```

### 2. Initialize Navi

To be able to use Navi and read the information in the sample vault, you will need to initialize it. This will create a default config file and create a sample vault in your `/Documents` folder. To initialize, simply run the following in your terminal:

```bash
obsidianavi
```

Navi is now ready to use. You can test it with:

```bash
obsidianavi --show-config
```

You should see the current configuration printed to the terminal.

> You only need to do this once per machine. After that, you can run Navi from anywhere.

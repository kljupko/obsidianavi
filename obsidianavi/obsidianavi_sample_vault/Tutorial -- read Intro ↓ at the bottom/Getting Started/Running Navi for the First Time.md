---
Function: Tutorial
Domain: Technology
Sub-domain: Tools
Subject: Navi
Area: Getting Started
Topic: Running Navi for the First Time
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

# Running Navi for the First Time

## Summary

Initial run instructions and what output to expect.

## Details

If you're reading this, it means you've installed the `obsidianavi` package and opened this sample vault in Obsidian.
You’re ready to run Navi.

> This process will only take a few seconds — and you’ll see results immediately.

### 🧭 Step-by-step Instructions

1. **Open a terminal or command prompt**  
   Use Terminal (macOS/Linux) or Command Prompt / PowerShell (Windows).

2. **Navigate to the `obsidianavi` folder**  
   > You can skip this step if you've installed `obsidianavi` using `pip`.
   
   In the terminal, use the `cd` command to move into the directory where you downloaded `obsidianavi`. For example:

	```bash
	cd path/to/your/obsidianavi
	```

	You should be in the same folder where a `README.md` file is located, along with the `/obsidianavi` folder.

3. **Initialize Navi**
   > If you're reading this in your vault, you've already done this step, so you can skip it.
   
   Running the following command will create a fresh configuration file and a sample vault for you to play with:
   
   ```bash
   python -m obsidianavi.cli
	```
   
   You should see an output in your terminal similar to the following:
   
   ```terminal
	[INFO] User config not found. Initializing from default.
	[INFO] Sample vault not found. Initializing in: /path/to/your/Documents/obsidianavi_sample_vault
	```
   
4. **Insert links into these notes** by running the following command:

	```python
	python -m obsidianavi.cli --write
	```

### ✅ What this does:

- Scans all `.md` files in the vault
- Identifies parents, siblings, and children for each note
- Replaces placeholder tags (like `%%​navi-p%%​`) with actual Obsidian links

---

### 🧪 What to expect:

- Each note will now have a block at the top showing where it fits in the structure
- If you're using Obsidian, you’ll see clickable links immediately
- No files are deleted or moved — only updated with links

---

### 🔁 Want to undo the changes?

If anything doesn’t look right, or you want to reverse the changes, you can always run:

```bash
python -m obsidianavi.cli --revert
```

This will undo the generated links and return each note to its original state.

> Once you're comfortable with this basic run, feel free to explore the rest of the tutorials (using the new links!) to learn about customization, configuration, and advanced features.

---
## What Now...
If you've successfully run the command, the Information notes should also be linked, so If you wish to know more about anything, see the [[Navi Intro]] note again, or you can keep exploring the various notes in the [[Tutorial]].
import json
import shutil
import os
import platform
from pathlib import Path

# --- Cross-platform config directory ---
def get_user_config_dir(app_name="obsidianavi"):
    system = platform.system()
    if system == "Windows":
        base = os.getenv("APPDATA", Path.home() / "AppData" / "Roaming")
    elif system == "Darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = Path.home() / ".config"
    return Path(base) / app_name

# --- Constants ---
DEFAULT_CONFIG_PATH = Path(__file__).parent / "obsidianavi_config.json"
USER_CONFIG_DIR = get_user_config_dir()
USER_CONFIG_PATH = USER_CONFIG_DIR / "obsidianavi_config.json"

SAMPLE_VAULT_NAME = "obsidianavi_sample_vault"
SAMPLE_VAULT_SRC = Path(__file__).parent / SAMPLE_VAULT_NAME
SAMPLE_VAULT_DEST = Path.home() / "Documents" / SAMPLE_VAULT_NAME

class ConfigManager:
    """
    Provides an interface to load, modify, reset, and display user configuration for ObsidiaNavi (or just "Navi" for short).

    Supports hierarchical key access and operations on both scalar and list-type values.
    """

    def __init__(self, user_path=USER_CONFIG_PATH, default_path=DEFAULT_CONFIG_PATH):
        """
        Initializes the configuration file by copying it to the system's hidden app folder (/.config, /AppData, or /Library).
        Creates a sample vault in the user's /Documents folder.
        """
        self.user_path = Path(user_path)
        self.default_path = Path(default_path)

        # Initialize config if missing
        if not self.user_path.exists():
            print(f"[INFO] User config not found. Initializing from default.")
            USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            shutil.copy(self.default_path, self.user_path)

        # Initialize sample vault if missing
        if not SAMPLE_VAULT_DEST.exists():
            print(f"[INFO] Sample vault not found. Initializing in: {SAMPLE_VAULT_DEST}")
            SAMPLE_VAULT_DEST.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(SAMPLE_VAULT_SRC, SAMPLE_VAULT_DEST)

        self.config = self.load()

    def load(self):
        """
        Loads the user's configuration JSON from disk.
        """
        with self.user_path.open("r", encoding="utf-8") as f:
            return json.load(f)


    def save(self):
        """
        Saves the current in-memory configuration state back to disk.
        """
        with self.user_path.open("w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def reset(self):
        """
        Resets the config file and the sample vault.
        """
        USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy(self.default_path, self.user_path)
        print(f"[INFO] Config reset to default.")

        if SAMPLE_VAULT_DEST.exists():
            shutil.rmtree(SAMPLE_VAULT_DEST)
        SAMPLE_VAULT_DEST.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SAMPLE_VAULT_SRC, SAMPLE_VAULT_DEST)
        print(f"[INFO] Sample vault reset in: {SAMPLE_VAULT_DEST}")

    def show(self):
        """
        Prints the current configuration as indented JSON.
        """
        print(json.dumps(self.config, indent=2))

    def get(self, key_path):
        """
        Retrieves and prints a nested value from the config using dot notation.

        Args:
            key_path (str): Dot-separated key path (e.g., "a.b.c").
        """
        keys = key_path.split(".")
        d = self.config
        for k in keys:
            if k not in d:
                print(f"[ERROR] Invalid config key path: {key_path}")
                return
            d = d[k]
        print(json.dumps({key_path: d}, indent=2))

    def set(self, item):
        """
        Sets a scalar (non-list) value using 'key.path=value' format.

        Args:
            item (str): The key and value to set.
        """
        key_path, value = item.split("=", 1)
        keys = key_path.split(".")
        d = self.config
        for k in keys[:-1]:
            if k not in d or not isinstance(d[k], dict):
                print(f"[ERROR] Invalid config key path: {key_path}")
                return
            d = d[k]
        final_key = keys[-1]
        if isinstance(d.get(final_key), list):
            print(f"[ERROR] Cannot use --set on list-type key: {key_path}. Use --add or --remove instead.")
            return
        d[final_key] = value
        print(f"Set '{key_path}' to '{value}'")

    def add(self, item):
        """
        Adds a value to a list-type key using 'key.path=value' format.

        Args:
            item (str): The key and value to append.
        """
        key_path, value = item.split("=", 1)
        keys = key_path.split(".")
        d = self.config
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        final_key = keys[-1]
        if final_key not in d:
            d[final_key] = []
        if not isinstance(d[final_key], list):
            print(f"[ERROR] Cannot add to non-list key: {key_path}")
            return
        d[final_key].append(value.strip())
        print(f"Added '{value.strip()}' to '{key_path}'")

    def remove(self, item):
        """
        Removes a value from a list-type key using 'key.path=value' format.

        Args:
            item (str): The key and value to remove.
        """
        key_path, value = item.split("=", 1)
        keys = key_path.split(".")
        d = self.config
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        final_key = keys[-1]
        if final_key not in d or not isinstance(d[final_key], list):
            print(f"[ERROR] Cannot remove from non-list key: {key_path}")
            return
        try:
            d[final_key].remove(value.strip())
            print(f"Removed '{value.strip()}' from '{key_path}'")
        except ValueError:
            print(f"[WARN] Value '{value.strip()}' not found in '{key_path}'")


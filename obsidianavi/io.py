from pathlib import Path
import json

def load_configuration(config_path):
    """
    Loads a JSON configuration file from the given path.

    Args:
        config_path (str or Path): Path to the configuration file.

    Returns:
        dict: Parsed JSON content as a dictionary.
    """
    config_path = Path(config_path)
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)

def read_note(note):
    """
    Reads and returns the full content of a markdown note from disk.

    Args:
        note (dict): A dictionary representing the note; must contain a 'path' key.

    Returns:
        str: Contents of the note file as a string.
    """
    with open(note["path"], "r", encoding="utf-8") as f:
        return f.read()

def write_note(note, content):
    """
    Writes a string of content to a markdown file specified in the note dictionary.

    Args:
        note (dict): A dictionary representing the note; must contain a 'path' key.
        content (str): The new content to write into the file.
    """
    with open(note["path"], "w", encoding="utf-8") as f:
        f.write(content)

def extract_frontmatter(file_path, delimiter='---'):
    """
    Extracts frontmatter from a markdown file using a YAML-style delimiter.

    Only supports single-line 'key: value' entries. Multiline or nested YAML is ignored.

    Args:
        file_path (str or Path): Path to the markdown file.
        delimiter (str): The line delimiter used to denote frontmatter boundaries (default: '---').

    Returns:
        dict: A flat dictionary of key-value pairs found in the frontmatter.
              Returns an empty dict if frontmatter is missing or malformed.
    """
    file_path = Path(file_path)
    with file_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != delimiter:
        return {}

    frontmatter = {}
    for line in lines[1:]:
        if line.strip() == delimiter:
            break
        if ':' in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter

def list_markdown_notes(vault_directory):
    """
    Recursively collects all markdown (.md) files in the given vault directory.

    Args:
        vault_directory (str or Path): Path to the root of the vault.

    Returns:
        list[Path]: List of paths to all markdown files found.
    """
    return list(Path(vault_directory).rglob("*.md"))

def parse_note_metadata(file_paths, hierarchy_keys):
    """
    Builds metadata for each markdown note based on its frontmatter and configured hierarchy keys.

    Determines the level of each note by how many hierarchy keys it uses.

    Args:
        file_paths (list[Path]): Paths to individual markdown files.
        hierarchy_keys (list[str]): Ordered list of keys used to determine note hierarchy.

    Returns:
        list[dict]: A list of note metadata dictionaries, each containing:
            - filename: Name of the file without extension
            - path: Full file path as string
            - frontmatter: Dict of parsed frontmatter
            - keys: List of hierarchy keys found
            - level: Integer representing note depth based on keys
    """
    notes = []
    for path in file_paths:
        front = extract_frontmatter(path)
        if not front:
            continue

        keys = [key for key in hierarchy_keys if key in front]

        note = {
            "filename": path.stem,
            "path": str(path),
            "frontmatter": front,
            "keys": keys,
            "level": len(keys)
        }
        notes.append(note)
    return notes


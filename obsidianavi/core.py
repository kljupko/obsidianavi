from pathlib import Path
from .io import list_markdown_notes, parse_note_metadata, write_note
from .relat import get_note_relationships
from .process import process_note_content, revert_note_content

def sort_note_relationships(note):
    """
    Sorts relationship lists (parents, siblings, children) in a note alphabetically.

    This ensures consistent link order in output, based on case-insensitive filename comparison.

    Args:
        note (dict): Dictionary containing note metadata and relationships.

    Returns:
        dict: Modified note dictionary with sorted relationships.
    """
    for key in ["parents", "siblings", "children"]:
        if key in note and isinstance(note[key], list):
            note[key] = sorted(note[key], key=str.lower)
    return note

def process_vault(config, write=False, target_notes=None, revert=False):
    """
    Processes or reverts notes in an Obsidian vault based on the given configuration.

    For each note:
      - Applies relationships (parents, siblings, children) and inserts template replacements.
      - Or reverts ObsidiaNavi-generated content back to its original tag format.

    Args:
        config (dict): Full ObsidiaNavi configuration dictionary.
        write (bool): If True, updated content is written back to disk.
        target_notes (list[str] or None): Filenames of notes to process; if None, all notes are processed.
        revert (bool): If True, performs reversion instead of generation.

    Returns:
        list[dict]: Metadata and relationship data for each processed note.
    """
    vault_directory = Path(config.get("vault_directory", ".")).expanduser().resolve()
    if not vault_directory.exists():
        print(f"[WARN] Vault directory not found: {vault_directory}")

    hierarchy_keys = config.get("hierarchy_keys", [])
    is_self_sibling = config.get("obsidianavi_link", {}).get("is_self_sibling") == "true"

    file_paths = list_markdown_notes(vault_directory)
    notes = parse_note_metadata(file_paths, hierarchy_keys)

    def is_excluded(note_path, config):
        """
        Checks whether a note should be excluded based on file and folder rules in the config.

        Args:
            note_path (str or Path): Path to the note.
            config (dict): Full configuration.

        Returns:
            bool: True if the note should be skipped.
        """
        path = Path(note_path)
        folder_parts = [p.as_posix() for p in path.parents]

        file_excludes = config.get("exclude_files", [])
        folder_excludes = config.get("exclude_folders", [])

        if any(ex in path.name for ex in file_excludes):
            return True

        if any(any(ex in folder for folder in folder_parts) for ex in folder_excludes):
            return True

        return False

    if target_notes:
        note_map = {n["filename"]: n for n in notes}
        missing = [n for n in target_notes if n not in note_map]
        if missing:
            raise ValueError(f"Notes not found: {', '.join(missing)}")
        selected_notes = [note_map[n] for n in target_notes]
    else:
        selected_notes = notes

    updated_notes = []

    for note in selected_notes:
        if not is_excluded(note["path"], config):
            if revert:
                new_content = revert_note_content(note, config)
            else:
                note = get_note_relationships(note, notes, include_self=is_self_sibling)
                note = sort_note_relationships(note)
                new_content = process_note_content(note, config)

            if write:
                write_note(note, new_content)

        updated_notes.append(note)

    return updated_notes


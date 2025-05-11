def keys_and_values_match(keys, fm1, fm2):
    """
    Checks whether all specified keys match between two frontmatter dictionaries.

    Args:
        keys (list[str]): Keys to compare.
        fm1 (dict): First note's frontmatter.
        fm2 (dict): Second note's frontmatter.

    Returns:
        bool: True if all keys exist in both and their values are equal.
    """
    for key in keys:
        if fm1.get(key) != fm2.get(key):
            return False
    return True

def find_related_notes(current, others, level_diff=0, include_self=False):
    """
    Finds related notes by comparing metadata and hierarchy level.

    The type of relationship is controlled via `level_diff`:
        -1 → parent (one level up, matching full parent keys)
         0 → sibling (same level, shared parent keys)
         1 → child (one level down, extends current key path)

    Args:
        current (dict): The current note.
        others (list[dict]): List of all candidate notes.
        level_diff (int): Target relationship level relative to current.
        include_self (bool): Whether to include the current note in the result (used for siblings).

    Returns:
        list[str]: List of related note filenames.
    """
    current_fm = current["frontmatter"]
    current_keys = current["keys"]
    current_level = current["level"]

    related = []
    for other in others:
        if not include_self and other["filename"] == current["filename"]:
            continue
        if other["level"] != current_level + level_diff:
            continue

        other_fm = other["frontmatter"]
        other_keys = other["keys"]

        if level_diff <= -1 and current_level > 1:
            # Parents match if they satisfy all current frontmatter up to current level
            if keys_and_values_match(other_keys, current_fm, other_fm):
                related.append(other["filename"])
        elif level_diff == 0:
            # Siblings share same parent structure (all keys except last)
            if current_level == 0:
                continue
            if keys_and_values_match(other_keys[:-1], current_fm, other_fm):
                related.append(other["filename"])
        elif level_diff >= 1:
            # Children match full current key path
            if keys_and_values_match(current_keys, current_fm, other_fm):
                related.append(other["filename"])

    return related

def find_parents(current, others):
    """
    Identifies all parent notes of the given note.

    A parent has one fewer hierarchy key and must match on all shared keys.

    Args:
        current (dict): The note being analyzed.
        others (list[dict]): All available notes.

    Returns:
        list[str]: Filenames of matching parent notes.
    """
    return find_related_notes(current, others, level_diff=-1)

def find_siblings(current, others, include_self=False):
    """
    Identifies sibling notes of the given note.

    Siblings exist at the same level and share the same parent keys.

    Args:
        current (dict): The note being analyzed.
        others (list[dict]): All available notes.
        include_self (bool): Whether to include the note itself in the results.

    Returns:
        list[str]: Filenames of matching sibling notes.
    """
    return find_related_notes(current, others, level_diff=0, include_self=include_self)

def find_children(current, others):
    """
    Identifies child notes of the given note.

    Children have one more hierarchy level and must share the full key path of the current note.

    Args:
        current (dict): The note being analyzed.
        others (list[dict]): All available notes.

    Returns:
        list[str]: Filenames of matching child notes.
    """
    return find_related_notes(current, others, level_diff=1)

def get_note_relationships(current, others, include_self=False):
    """
    Adds relationship data to a note by finding its parents, siblings, and children.

    Args:
        current (dict): The note to enrich.
        others (list[dict]): All available notes.
        include_self (bool): Whether to include the current note in its sibling list.

    Returns:
        dict: A new note dictionary with added 'parents', 'siblings', and 'children' lists.
    """
    return {
        **current,
        "parents": find_parents(current, others),
        "siblings": find_siblings(current, others, include_self),
        "children": find_children(current, others)
    }


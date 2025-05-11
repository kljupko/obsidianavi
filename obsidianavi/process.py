import re
from datetime import datetime, timedelta
from .io import read_note

def process_note_content(note, config):
    """
    Updates a note’s content by replacing placeholder tags with actual navigation data.

    This includes:
    - Wrapping all known template tags in identifiable open/close markers.
    - Inserting Obsidian links for parents, siblings, and children.
    - Replacing tag counts with actual numbers of related notes.
    - Generating links for relative dates (today, yesterday, tomorrow) based on frontmatter.

    Args:
        note (dict): Metadata and relationships for the note.
        config (dict): Complete ObsidiaNavi configuration object.

    Returns:
        str: Transformed note content with substitutions applied.
    """
    note_name = note.get("filename")
    content = read_note(note)

    def wrap_template_tags(content, config):
        """
        Replaces plain template tags in the note with wrapped versions using open/close markers.
        """
        tags = config.get("template_tags")
        replacements = {
            tags.get("parents"): (tags.get("open_parents"), tags.get("close_parents")),
            tags.get("siblings"): (tags.get("open_siblings"), tags.get("close_siblings")),
            tags.get("children"): (tags.get("open_children"), tags.get("close_children")),
            tags.get("parents_count"): (tags.get("open_parents_count"), tags.get("close_parents_count")),
            tags.get("siblings_count"): (tags.get("open_siblings_count"), tags.get("close_siblings_count")),
            tags.get("children_count"): (tags.get("open_children_count"), tags.get("close_children_count")),
            tags.get("yesterday"): (tags.get("open_yesterday"), tags.get("close_yesterday")),
            tags.get("today"): (tags.get("open_today"), tags.get("close_today")),
            tags.get("tomorrow"): (tags.get("open_tomorrow"), tags.get("close_tomorrow"))
        }

        for tag, (start, end) in replacements.items():
            pattern = re.escape(tag)
            wrapped = f"{start}{tag}{end}"
            content = re.sub(pattern, wrapped, content)
            content = content.replace(tag, "")

        return content

    def extract_related_note_names(note):
        """
        Extracts parent, sibling, and child filenames from the note metadata.

        Returns:
            dict: Dictionary with lists of related note names.
        """
        return {
            "parents": note.get("parents", []),
            "siblings": note.get("siblings", []),
            "children": note.get("children", [])
        }

    def format_filenames(filenames, note_name, config):
        """
        Converts raw filenames into formatted Obsidian links using ObsidiaNavi link settings.

        Returns:
            dict: Keys are relationship types, values are formatted lists of links.
        """
        def format_group(names, note_name, italic, linked, space):
            result = []
            for name in names:
                display = name
                if name == note_name:
                    if linked:
                        display = f"[[{display}]]"
                    if italic:
                        display = f"*{display}*"
                else:
                    display = f"[[{display}]]"
                display = display.replace(" ", space)
                result.append(display)
            return result

        navi_links = config.get("obsidianavi_link")
        italic = navi_links.get("is_self_italic", "false").lower() == "true"
        linked = navi_links.get("is_self_linked", "false").lower() == "true"
        nbsp = navi_links.get("use_nonbreaking_space") == "true"
        space = "\u00A0" if nbsp else " "

        return {
            "parents": format_group(filenames.get("parents", []), note_name, italic, linked, space),
            "siblings": format_group(filenames.get("siblings", []), note_name, italic, linked, space),
            "children": format_group(filenames.get("children", []), note_name, italic, linked, space)
        }

    def replace_data(note, content, links, config):
        """
        Applies all replacements to the note content:
        - Related links
        - Relationship counts
        - Date-relative references
        """

        def replace_links(content, links, config):
            sep = config["obsidianavi_link"]["separator"]
            space = "\u00A0" if config["obsidianavi_link"].get("use_nonbreaking_space") == "true" else " "
            joined_sep = f"{space}{sep} "

            tags = config["template_tags"]
            sections = {
                "parents": (tags["open_parents"], tags["close_parents"]),
                "siblings": (tags["open_siblings"], tags["close_siblings"]),
                "children": (tags["open_children"], tags["close_children"]),
            }

            for key, (start, end) in sections.items():
                joined = joined_sep.join(links.get(key, []))
                pattern = rf"{re.escape(start)}.*?{re.escape(end)}"
                replacement = f"{start}{joined}{end}"
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            return content

        def replace_counts(content, links, config):
            tags = config["template_tags"]
            sections = {
                "parents": (tags["open_parents_count"], tags["close_parents_count"]),
                "siblings": (tags["open_siblings_count"], tags["close_siblings_count"]),
                "children": (tags["open_children_count"], tags["close_children_count"]),
            }

            for key, (start, end) in sections.items():
                count = str(len(links.get(key, 0)))
                pattern = rf"{re.escape(start)}.*?{re.escape(end)}"
                replacement = f"{start}{count}{end}"
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            return content

        def get_note_date(note, config):
            """
            Attempts to extract and parse a date from the note's frontmatter.

            Returns:
                (date, str): A datetime.date object and the date format string, or (None, None) on failure.
            """
            date_key = config["date_settings"]["date_property_name"]
            fmt = config["date_settings"]["date_format"]
            raw = note.get("frontmatter", {}).get(date_key)
            if not raw:
                return None, None
            try:
                date_obj = datetime.strptime(raw, fmt)
                return date_obj.date(), fmt
            except ValueError:
                return None, None

        def replace_dates(note, content, date, fmt, config):
            """
            Replaces wrapped date tags with Obsidian links for today, yesterday, and tomorrow.

            If the target date note isn't listed as a sibling, the alias is struck through.

            Returns:
                str: Updated content with date tags replaced.
            """
            if date is None:
                return content

            tags = config["template_tags"]
            aliases = config["date_settings"].get("aliases", {})
            offsets = {
                "yesterday": (-1, tags["open_yesterday"], tags["close_yesterday"]),
                "today": (0, tags["open_today"], tags["close_today"]),
                "tomorrow": (1, tags["open_tomorrow"], tags["close_tomorrow"]),
            }

            def link_for_day(offset, label):
                target = date + timedelta(days=offset)
                date_str = target.strftime(fmt)
                if label and (date_str not in note.get("siblings", [])):
                    return f"~~{label}~~"
                return f"[[{date_str}|{label}]]" if label else f"[[{date_str}]]"

            for key, (offset, start, end) in offsets.items():
                alias = aliases.get(key)
                date_link = link_for_day(offset, alias)
                pattern = rf"{re.escape(start)}.*?{re.escape(end)}"
                replacement = f"{start}{date_link}{end}"
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)

            return content

        content = replace_links(content, links, config)
        content = replace_counts(content, links, config)
        date, date_format = get_note_date(note, config)
        content = replace_dates(note, content, date, date_format, config)
        return content

    content = wrap_template_tags(content, config)
    filenames = extract_related_note_names(note)
    links = format_filenames(filenames, note_name, config)
    content = replace_data(note, content, links, config)

    return content

def revert_note_content(note, config):
    """
    Restores a note’s content to its original form by removing ObsidiaNavi's wrapping tags.

    This replaces each wrapped tag block with its unwrapped placeholder tag.

    Args:
        note (dict): A dictionary containing the 'path' of the note to revert.
        config (dict): Full configuration including template tag definitions.

    Returns:
        str: Note content with all ObsidiaNavi-generated blocks reverted.
    """
    content = read_note(note)
    tags = config.get("template_tags", {})

    for key, tag in tags.items():
        open_tag = tags.get(f"open_{key}")
        close_tag = tags.get(f"close_{key}")
        if open_tag and close_tag:
            pattern = rf"{re.escape(open_tag)}.*?{re.escape(close_tag)}"
            content = re.sub(pattern, tag, content, flags=re.DOTALL)

    return content


from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CLIArgs:
    """
    Holds the parsed command-line options for ObsidiaNavi (or just "Navi" for short).

    All flags and their corresponding values (if applicable) are stored in this structured object.
    Fields are initialized to appropriate defaults and populated during parsing.
    """
    target_notes: Optional[List[str]] = None  # List of note filenames to process
    write_to_notes: bool = False              # Whether to apply changes to disk
    set_items: Optional[List[str]] = None     # List of key=value strings to set scalar config values
    add_items: Optional[List[str]] = None     # List of key=value strings to append to list-type config fields
    remove_items: Optional[List[str]] = None  # List of key=value strings to remove from list-type config fields
    reset_config: bool = False                # If True, reset config to default
    show_config: bool = False                 # If True, display current config
    get_key: Optional[str] = None             # Dot-path string for retrieving a config value
    revert_notes: bool = False                # If True, revert ObsidiaNavi-modified tags to original placeholders
    help_requested: bool = False              # If True, show help and exit

def parse_args(argv) -> CLIArgs:
    """
    Parses a list of command-line arguments and returns a populated CLIArgs object.

    Supports flags for configuration management, file targeting, note processing,
    and command-line help.

    Args:
        argv (List[str]): Command-line arguments, excluding the script name.

    Returns:
        CLIArgs: Object containing structured representation of CLI options.
    """
    args = CLIArgs(set_items=[], add_items=[], remove_items=[])
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--notes":
            i += 1
            args.target_notes = []
            while i < len(argv) and not argv[i].startswith("--"):
                args.target_notes.append(argv[i])
                i += 1
        elif arg == "--write":
            args.write_to_notes = True
            i += 1
        elif arg == "--set":
            i += 1
            while i < len(argv) and not argv[i].startswith("--"):
                args.set_items.append(argv[i])
                i += 1
        elif arg == "--add":
            i += 1
            while i < len(argv) and not argv[i].startswith("--"):
                args.add_items.append(argv[i])
                i += 1
        elif arg == "--remove":
            i += 1
            while i < len(argv) and not argv[i].startswith("--"):
                args.remove_items.append(argv[i])
                i += 1
        elif arg == "--reset":
            args.reset_config = True
            i += 1
        elif arg == "--show-config":
            args.show_config = True
            i += 1
        elif arg == "--get":
            i += 1
            if i < len(argv):
                args.get_key = argv[i]
                i += 1
        elif arg == "--revert":
            args.revert_notes = True
            i += 1
        elif arg == "--help":
            args.help_requested = True
            i += 1
        else:
            # Unknown argument, skip
            i += 1
    return args


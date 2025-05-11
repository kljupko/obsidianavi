import sys
from pathlib import Path
from .core import process_vault
from .config_manager import ConfigManager, USER_CONFIG_PATH, DEFAULT_CONFIG_PATH
from .arg_parser import parse_args

def print_help():
    """
    Outputs a detailed help message describing all supported CLI options.

    This function is triggered when the user passes the --help flag.
    """
    help_text = """
ObsidiaNavi CLI (or just "Navi" for short) - Obsidian note navigation tool
This tool allows:
  - automatic generation of links between parent/ sibling/ child nodes based on metadata
  - automatic generation of links for Yesterday, Today, Tomorrow daily notes based on metadata
  - altering behavior based on obsidianavi_config.json file

USAGE:
  python -m obsidianavi.cli [OPTIONS]

OPTIONS:
  --help
      Show this help message and exit.

  --write
      Write changes to files after processing.
      Example:
        python -m obsidianavi.cli --write

  --revert
      Revert Navi placeholders back to their original form.
      Example:
        python -m obsidianavi.cli --revert --notes NoteA NoteB

  --notes "Note1" "Note2"
      Specify which notes to process or revert.
      Example:
        python -m obsidianavi.cli --write --notes "coding in python" "recursion"

  --reset
      Restore default configuration to ~/.config/obsidianavi/obsidianavi_config.json.
      Example:
        python -m obsidianavi.cli --reset

  --show-config
      Print the current configuration in JSON format.

  --get key.path
      Get a specific config value by nested path.
      Example:
        python -m obsidianavi.cli --get date_settings.date_format

  --set key.path=value
      Set a scalar config value.
      Example:
        python -m obsidianavi.cli --set vault_directory=./my_vault

  --add key.path=value
      Add a value to a list-type config field.
      Example:
        python -m obsidianavi.cli --add exclude=my_vault/Templates

  --remove key.path=value
      Remove a value from a list-type config field.
      Example:
        python -m obsidianavi.cli --remove exclude=./my_vault/Templates

NOTES:
  - Use dot-notation for nested config (e.g., date_settings.date_format).
  - Changes via --set/--add/--remove are saved immediately.
  - The exclude lists work as substring filters *, meaning that:
    - excluding a "README" file excludes any notes containing "README" in the name:
      - "README"
      - "README please"
      - "don't README"
    - excluding a "Template" folder excludes any folders with "Template" in the name:
      - "Templates"
      - "Templates/Tasks"
    * the excludes may behave differently based on whether your system is case-sensitive or not
"""
    print(help_text)

def did_perform_action(args):
    """
    Determines whether any action-related flags were provided by the user.

    Args:
        args (CLIArgs): Parsed command-line arguments.

    Returns:
        bool: True if any actionable flags were passed.
    """
    return any([
        args.write_to_notes,
        args.revert_notes,
        args.get_key,
        args.set_items,
        args.add_items,
        args.remove_items,
        args.show_config,
        args.reset_config
    ])

def main():
    """
    Main entry point for the ObsidiaNavi CLI.

    - Parses command-line arguments.
    - Dispatches actions related to configuration or note processing.
    - If no actions are specified, prints a usage message.
    """
    args = parse_args(sys.argv[1:])
    config_mgr = ConfigManager(USER_CONFIG_PATH, DEFAULT_CONFIG_PATH)

    if args.help_requested:
        print_help()
        return

    # Configuration-related commands
    if args.reset_config:
        config_mgr.reset()
        return

    if args.show_config:
        config_mgr.show()
        return

    if args.get_key:
        config_mgr.get(args.get_key)
        return

    if args.set_items:
        for item in args.set_items:
            config_mgr.set(item)

    if args.add_items:
        for item in args.add_items:
            config_mgr.add(item)

    if args.remove_items:
        for item in args.remove_items:
            config_mgr.remove(item)

    # Apply config changes if any were made
    if args.set_items or args.add_items or args.remove_items:
        config_mgr.save()

    # Note processing commands
    if args.write_to_notes or args.revert_notes:
        try:
            process_vault(
                config_mgr.config,
                write=True,
                target_notes=args.target_notes,
                revert=args.revert_notes
            )
        except ValueError as e:
            import json
            print(json.dumps({"error": str(e)}, indent=2))
        return

    # No valid actions were triggered
    if not did_perform_action(args):
        print("[INFO] No action specified. Use --help for available options.")

if __name__ == "__main__":
    main()


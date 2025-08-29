#python tree_printer.py /path/to/Folder --depth 3

import os
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def print_tree(root_path, prefix="", depth=None, level=0):
    if depth is not None and level >= depth:
        return

    try:
        entries = [e for e in sorted(os.listdir(root_path)) if not e.startswith('.')]
    except PermissionError:
        print(prefix + Fore.RED + "⛔ Permission denied")
        return

    entries_count = len(entries)

    for index, entry in enumerate(entries):
        full_path = os.path.join(root_path, entry)
        connector = "└─ " if index == entries_count - 1 else "├─ "
        is_dir = os.path.isdir(full_path)

        # Color formatting
        entry_display = (
            Fore.BLUE + entry + "/" + Style.RESET_ALL if is_dir
            else Fore.GREEN + entry + Style.RESET_ALL
        )

        print(prefix + connector + entry_display)

        if is_dir:
            extension = "    " if index == entries_count - 1 else "│   "
            print_tree(full_path, prefix + extension, depth, level + 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print directory tree structure.")
    parser.add_argument("folder", help="Path to the folder to describe")
    parser.add_argument("--depth", type=int, default=None, help="Limit tree depth")
    args = parser.parse_args()

    folder_path = os.path.abspath(args.folder)
    folder_name = os.path.basename(folder_path)

    print(Fore.YELLOW + folder_name + "/" + Style.RESET_ALL)
    print_tree(folder_path, depth=args.depth)

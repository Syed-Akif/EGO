"""
Folder Operations
"""

import os

from app.filesystem.paths import FOLDERS
from pathlib import Path


def create_folder(name: str) -> bool:
    """
    Creates a folder in the current working directory.

    Returns:
        True if successful.
        False if the folder already exists.
    """

    path = Path.cwd() / name

    if path.exists():
        return False

    path.mkdir()

    return True

def open_folder(name: str) -> bool:
    """
    Opens a known folder.

    Returns:
        True if opened.
        False if unknown.
    """

    folder = FOLDERS.get(name.lower())

    if folder is None:
        return False

    os.startfile(folder)

    return True

def rename_folder(old_name: str, new_name: str) -> bool:
    """
    Renames a folder.
    """

    old_path = Path.cwd() / old_name
    new_path = Path.cwd() / new_name

    if not old_path.exists():
        return False

    if new_path.exists():
        return False

    try:
        old_path.rename(new_path)
        return True

    except OSError:
        return False
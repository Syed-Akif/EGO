"""
File operations for EGO.
"""

from pathlib import Path


def create_file(name: str) -> bool:
    
    """
    Creates an empty file in the current working directory.
    """

    path = Path.cwd() / name

    if path.exists():
        return False

    path.touch()

    return True

def read_file(name: str) -> str | None:
    """
    Reads a text file.

    Returns:
        File contents if successful.
        None if the file doesn't exist.
    """

    path = Path.cwd() / name

    if not path.exists():
        return None

    return path.read_text(encoding="utf-8")

def write_file(name: str, content: str) -> bool:
    """
    Writes text to a file.

    Returns:
        True if successful.
        False otherwise.
    """

    path = Path.cwd() / name

    try:
        path.write_text(content, encoding="utf-8")
        return True

    except OSError:
        return False
    
def append_file(name: str, content: str) -> bool:
    """
    Appends text to a file.

    Returns:
        True if successful.
        False otherwise.
    """

    path = Path.cwd() / name

    try:
        with path.open("a", encoding="utf-8") as file:
            file.write("\n" + content)

        return True

    except OSError:
        return False

def rename_file(old_name: str, new_name: str) -> bool:
    """
    Renames a file.

    Returns:
        True if successful.
        False if the source file doesn't exist
        or the destination already exists.
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
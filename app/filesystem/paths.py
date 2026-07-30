"""
Filesystem Paths

Provides common Windows user folders.
"""

from pathlib import Path


HOME = Path.home()

DESKTOP = HOME / "Desktop"

DOCUMENTS = HOME / "Documents"

DOWNLOADS = HOME / "Downloads"

PICTURES = HOME / "Pictures"

MUSIC = HOME / "Music"

VIDEOS = HOME / "Videos"


FOLDERS = {
    "desktop": DESKTOP,
    "documents": DOCUMENTS,
    "downloads": DOWNLOADS,
    "pictures": PICTURES,
    "music": MUSIC,
    "videos": VIDEOS,
}
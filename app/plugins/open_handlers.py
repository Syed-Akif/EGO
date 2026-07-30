"""
Open Handler Chain

Registers every handler capable of opening something.
"""

from app.filesystem.manager import FileSystemManager

# More handlers will be added here later
# Example:
# from app.browser.manager import BrowserManager
# from app.applications.manager import ApplicationManager

HANDLERS = [
    FileSystemManager(),
]
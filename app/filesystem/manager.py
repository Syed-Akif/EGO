"""
Filesystem Manager
"""

from app.filesystem.folders import (
    open_folder,
    create_folder,
    rename_folder,
    delete_folder,
)

from app.filesystem.files import (
    create_file,
    read_file,
    write_file,
    append_file,
    rename_file,
    delete_file,
)

class FileSystemManager:
    """
    Coordinates all filesystem operations.
    """

    def open(self, target: str) -> bool:
        return open_folder(target)

    def create_folder(self, name: str) -> bool:
        return create_folder(name)

    def create_file(self, name: str) -> bool:
        return create_file(name)

    def read_file(self, name: str):
        return read_file(name)
    
    def write_file(self, name: str, content: str) -> bool:
        return write_file(name, content)
    
    def append_file(self, name: str, content: str) -> bool:
        return append_file(name, content)
    
    def rename_file(self, old_name: str, new_name: str) -> bool:
        return rename_file(old_name, new_name)

    def rename_folder(self, old_name: str, new_name: str) -> bool:
        return rename_folder(old_name, new_name)
    
    def delete_file(self, name: str) -> bool:
        return delete_file(name)

    def delete_folder(self, name: str) -> bool:
        return delete_folder(name)
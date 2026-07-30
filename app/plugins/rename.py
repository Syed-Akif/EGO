INTENT = "rename"

from app.core.response import Response
from app.filesystem.manager import FileSystemManager

manager = FileSystemManager()


def execute(command):
    """
    Handles:
    rename file <old> <new>
    rename folder <old> <new>
    """

    if len(command.arguments) < 2:
        return Response(
            success=False,
            message="Usage: rename <file|folder> <old_name> <new_name>"
        )

    old_name = command.arguments[0]
    new_name = command.arguments[1]

    if command.target == "file":

        if manager.rename_file(old_name, new_name):
            return Response(
                True,
                f"File renamed to '{new_name}'."
            )

        return Response(
            False,
            "Rename failed."
        )

    elif command.target == "folder":

        if manager.rename_folder(old_name, new_name):
            return Response(
                True,
                f"Folder renamed to '{new_name}'."
            )

        return Response(
            False,
            "Rename failed."
        )

    return Response(
        False,
        "I can currently rename only files and folders."
    )
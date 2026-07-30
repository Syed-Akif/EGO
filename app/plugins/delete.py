INTENT = "delete"

from app.core.response import Response
from app.filesystem.manager import FileSystemManager

manager = FileSystemManager()


def execute(command):
    """
    Handles:
    delete file <name>
    delete folder <name>
    """

    if not command.arguments:
        return Response(
            success=False,
            message="Please provide a file or folder name."
        )

    name = command.arguments[0]

    if command.target == "file":

        if manager.delete_file(name):
            return Response(
                True,
                f"File '{name}' deleted successfully."
            )

        return Response(
            False,
            "Delete failed."
        )

    elif command.target == "folder":

        if manager.delete_folder(name):
            return Response(
                True,
                f"Folder '{name}' deleted successfully."
            )

        return Response(
            False,
            "Delete failed."
        )

    return Response(
        False,
        "I can currently delete only files and folders."
    )
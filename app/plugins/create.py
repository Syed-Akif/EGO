INTENT = "create"

from app.core.response import Response
from app.filesystem.manager import FileSystemManager

manager = FileSystemManager()


def execute(command):

    if not command.arguments:
        return Response(
            success=False,
            message="Please provide a name."
        )

    name = " ".join(command.arguments)

    if command.target == "folder":

        if manager.create_folder(name):
            return Response(True, f"Folder '{name}' created successfully.")

        return Response(False, f"Folder '{name}' already exists.")

    elif command.target == "file":

        if manager.create_file(name):
            return Response(True, f"File '{name}' created successfully.")

        return Response(False, f"File '{name}' already exists.")

    return Response(
        success=False,
        message="I can currently create folders and files only."
    )
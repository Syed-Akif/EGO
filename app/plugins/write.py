INTENT = "write"

from app.core.response import Response
from app.filesystem.manager import FileSystemManager

manager = FileSystemManager()


def execute(command):
    """
    Handles:
    write file <filename> <content>
    """

    if command.target != "file":
        return Response(
            success=False,
            message="I can currently write only to files."
        )

    if len(command.arguments) < 2:
        return Response(
            success=False,
            message="Usage: write file <filename> <content>"
        )

    filename = command.arguments[0]
    content = " ".join(command.arguments[1:])

    if manager.write_file(filename, content):
        return Response(
            success=True,
            message=f"Successfully wrote to '{filename}'."
        )

    return Response(
        success=False,
        message=f"Failed to write to '{filename}'."
    )
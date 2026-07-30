INTENT = "append"

from app.core.response import Response
from app.filesystem.manager import FileSystemManager

manager = FileSystemManager()


def execute(command):
    """
    Handles:
    append file <filename> <content>
    """

    if command.target != "file":
        return Response(
            success=False,
            message="I can currently append only to files."
        )

    if len(command.arguments) < 2:
        return Response(
            success=False,
            message="Usage: append file <filename> <content>"
        )

    filename = command.arguments[0]
    content = " ".join(command.arguments[1:])

    if manager.append_file(filename, content):
        return Response(
            success=True,
            message=f"Successfully appended to '{filename}'."
        )

    return Response(
        success=False,
        message=f"Failed to append to '{filename}'."
    )
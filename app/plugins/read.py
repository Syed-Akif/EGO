INTENT = "read"

from app.core.response import Response
from app.filesystem.manager import FileSystemManager

manager = FileSystemManager()


def execute(command):

    if command.target != "file":
        return Response(
            success=False,
            message="I can currently read files only."
        )

    if not command.arguments:
        return Response(
            success=False,
            message="Please provide a file name."
        )

    filename = " ".join(command.arguments)

    content = manager.read_file(filename)

    if content is None:
        return Response(
            success=False,
            message=f"File '{filename}' not found."
        )

    return Response(
        success=True,
        message=content
    )
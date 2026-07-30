INTENT = "system"

from app.core.response import Response
from app.windows.manager import WindowsManager

manager = WindowsManager()


def execute(command):
    """
    Handles system operations.
    """

    if command.action == "lock":

        if manager.lock():
            return Response(
                True,
                "Computer locked."
            )

        return Response(
            False,
            "Unable to lock the computer."
        )

    return Response(
        False,
        "Unknown system command."
    )
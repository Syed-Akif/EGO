INTENT = "power"

from app.core.response import Response
from app.windows.manager import WindowsManager

manager = WindowsManager()


def execute(command):

    if command.intent != "power":
        return Response(
            False,
            "Invalid power command."
        )

    if command.raw.lower() == "lock computer":

        if manager.lock():
            return Response(
                True,
                "Computer locked successfully."
            )

        return Response(
            False,
            "Unable to lock the computer."
        )

    if command.raw.lower() == "shutdown computer":

        if manager.shutdown():
            return Response(
                True,
                "Shutting down computer..."
            )

        return Response(
            False,
            "Unable to shut down the computer."
        )

    if command.raw.lower() == "restart computer":

        if manager.restart():
            return Response(
                True,
                "Restarting computer..."
            )

        return Response(
            False,
            "Unable to restart the computer."
        )

    if command.raw.lower() == "sleep computer":

        if manager.sleep():
            return Response(
                True,
                "Putting computer to sleep..."
            )

        return Response(
            False,
            "Unable to put the computer to sleep."
        )

    return Response(
        False,
        "Unknown power command."
    )
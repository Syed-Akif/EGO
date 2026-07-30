INTENT = "open"

from app.core.response import Response
from app.plugins.open_handlers import HANDLERS

# Existing handlers
from app.plugins.applications import execute as open_application
from app.plugins.browser import execute as open_browser


def execute(command):

    # Try applications
    response = open_application(command)
    if response:
        return response

    # Try browser
    response = open_browser(command)
    if response:
        return response

    # Try every registered handler
    for handler in HANDLERS:

        if handler.open(command.target):

            return Response(
                success=True,
                message=f"Opening {command.target}..."
            )

    return Response(
        success=False,
        message=f"I don't know how to open '{command.target}'."
    )
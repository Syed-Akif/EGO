from app.plugins import applications
from app.plugins import browser

from app.core.response import Response


def execute(command):

    # Try opening as an application
    response = applications.execute(command)

    if response:
        return response

    # Try opening as a website
    response = browser.execute(command)

    if response:
        return response

    # Nothing matched
    return Response(
        success=False,
        message=f"I don't know '{command.target}'."
    )
import subprocess

from app.core.response import Response
from app.config.apps import APPS


def execute(command):

    if not command.arguments:
        return Response(
            success=False,
            message="No application specified."
        )

    app_name = command.arguments[0].lower()

    app = APPS.get(app_name)

    if not app:
        return Response(
            success=False,
            message=f"I don't know the application '{app_name}'."
        )

    try:

        subprocess.Popen(f"start {app}", shell=True)

        return Response(
            success=True,
            message=f"Opening {app_name}..."
        )

    except Exception as e:

        return Response(
            success=False,
            message=str(e)
        )
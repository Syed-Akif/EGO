import subprocess

from app.core.response import Response
from app.config.apps import APPS


def execute(command):

    if not command.target:
        return None

    app = APPS.get(command.target.lower())

    if not app:
        return None

    try:

        subprocess.Popen(f"start {app}", shell=True)

        return Response(
            success=True,
            message=f"Opening {command.target}..."
        )

    except Exception as e:

        return Response(
            success=False,
            message=str(e)
        )
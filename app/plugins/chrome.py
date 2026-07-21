import subprocess

from app.core.response import Response


def execute():
    try:
        subprocess.Popen("start chrome", shell=True)

        return Response(
            success=True,
            message="Opening Google Chrome..."
        )

    except Exception as e:
        return Response(
            success=False,
            message=str(e)
        )
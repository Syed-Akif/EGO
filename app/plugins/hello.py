from app.core.response import Response


def execute():
    return Response(
        success=True,
        message="Hello! I am EGO."
    )
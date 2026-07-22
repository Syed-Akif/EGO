INTENT = "hello"
from app.core.response import Response



def execute(command):
    return Response(
        success=True,
        message="Hello! I am EGO."
    )
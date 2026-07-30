INTENT = "version"

from app.core.response import Response
from app.core.version import (
    FULL_NAME,
    VERSION,
    CODENAME,
    BUILD,
    AUTHOR,
)


def execute(command):

    message = f"""
{FULL_NAME}

Version   : {VERSION}
Codename  : {CODENAME}
Build     : {BUILD}
Author    : {AUTHOR}
"""

    return Response(
        success=True,
        message=message.strip()
    )
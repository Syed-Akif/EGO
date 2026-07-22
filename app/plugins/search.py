import webbrowser
from urllib.parse import quote_plus
from app.core.response import Response


def execute(command):

    if not command.target:
        return None

    query = quote_plus(" ".join(command.arguments))

    target = command.target.lower()

    if target == "google":

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    elif target == "youtube":

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

    elif target == "github":

        webbrowser.open(
            f"https://github.com/{query}"
        )

    else:

        return Response(
            success=False,
            message=f"Search is not supported for '{target}'."
        )

    return Response(
        success=True,
        message=f"Searching {target}..."
    )
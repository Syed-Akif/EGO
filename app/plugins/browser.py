import webbrowser
from urllib.parse import quote_plus

from app.core.response import Response
from app.config.websites import WEBSITES


def execute(command):

    if not command.target:
        return None

    website = WEBSITES.get(command.target.lower())

    if not website:
        return None

    if not command.arguments:

        webbrowser.open(website)

    else:

        query = quote_plus(" ".join(command.arguments))

        if command.target == "google":

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

        elif command.target == "youtube":

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        elif command.target == "github":

            webbrowser.open(
                f"https://github.com/{query}"
            )

        else:

            webbrowser.open(website)

    return Response(
        success=True,
        message=f"Opening {command.target}..."
    )
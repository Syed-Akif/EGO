from app.core.registry import PLUGINS
from app.core.response import Response


class Router:

    def route(self, command):

        plugin = PLUGINS.get(command.intent)

        if plugin:
            return plugin.execute(command)

        return Response(
            success=False,
            message="Sorry, I don't understand that command yet."
        )
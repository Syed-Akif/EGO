from app.core.registry import PLUGINS
from app.core.response import Response
from app.core.context import context


class Router:

    def route(self, command):

        plugin = PLUGINS.get(command.intent)

        if plugin:

          response = plugin.execute(command)

          context.last_intent = command.intent
          context.last_target = command.target
          context.last_arguments = command.arguments
          context.last_response = response.message

        print("\n------ CONTEXT ------")
        print(context)
        print("---------------------\n")

        return response
from app.core.plugin_manager import PluginManager
from app.core.response import Response
from app.core.context import context

plugin_manager = PluginManager()


class Router:

    def route(self, command):

        plugin = plugin_manager.get_plugin(command.intent)

        if not plugin:
            return Response(
                success=False,
                message=f"I don't understand '{command.intent}'."
            )

        response = plugin.execute(command)

        # Update Context
        context.last_intent = command.intent
        context.last_target = command.target
        context.last_arguments = command.arguments
        context.last_response = response.message

        return response
from app.core.context import context


class Brain:

    def think(self, command):

        # Context-aware search
        if command.intent == "search":

            if command.target is None:

                command.target = context.last_target

        return command
from app.core.intent_resolver import resolve
from app.core.command import Command


class Parser:

    def parse(self, text: str) -> Command:

        text = text.strip()

        parts = text.split()

        if not parts:
            return Command(
                raw="",
                intent="",
                target=None,
                arguments=[]
            )

        intent = resolve(parts[0])

        target = None
        arguments = []

        # ----------------------------------
        # Search command parsing
        # ----------------------------------

        if intent == "search":

            SEARCH_TARGETS = {
                "google",
                "youtube",
                "github",
            }

            if len(parts) >= 2:

                possible_target = parts[1].lower()

                if possible_target in SEARCH_TARGETS:

                    target = possible_target
                    arguments = parts[2:]

                else:

                    arguments = parts[1:]

        # ----------------------------------
        # Default parsing
        # ----------------------------------

        else:

            if len(parts) >= 2:
                target = parts[1].lower()

            if len(parts) >= 3:
                arguments = parts[2:]

        return Command(
            raw=text,
            intent=intent,
            target=target,
            arguments=arguments,
        )
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

        intent = parts[0].lower()

        target = None

        arguments = []

        if len(parts) >= 2:

            target = parts[1].lower()

        if len(parts) >= 3:
            
            arguments = parts[2:]

        return Command(
            raw=text,
            intent=intent,
            target=target,
            arguments=arguments
        )
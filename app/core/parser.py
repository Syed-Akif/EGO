from app.core.command import Command


class Parser:

    def parse(self, text: str) -> Command:

        text = text.strip()

        parts = text.split()

        intent = parts[0].lower()

        arguments = parts[1:]

        print("DEBUG")
        print("Intent:", intent)
        print("Arguments:", arguments)

        return Command(
            raw=text,
            intent=intent,
            arguments=arguments
        )
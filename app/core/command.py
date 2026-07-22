from dataclasses import dataclass


@dataclass
class Command:
    """
    Represents a parsed user command.
    """

    raw: str

    intent: str

    target: str | None

    arguments: list[str]
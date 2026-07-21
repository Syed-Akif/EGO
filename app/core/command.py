from dataclasses import dataclass


@dataclass
class Command:
    """
    Represents a command issued by the user.
    """

    raw: str
    intent: str = ""
    arguments: list[str] | None = None
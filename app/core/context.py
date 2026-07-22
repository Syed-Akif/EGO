from dataclasses import dataclass, field


@dataclass
class Context:

    last_intent: str | None = None

    last_target: str | None = None

    last_arguments: list[str] = field(default_factory=list)

    last_response: str | None = None


context = Context()
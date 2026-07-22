INTENT_ALIASES = {

    # Open
    "open": "open",
    "launch": "open",
    "start": "open",
    "run": "open",
    "execute": "open",

    # Close (future)
    "close": "close",
    "exit": "close",
    "quit": "close",
    "terminate": "close",
    "kill": "close",

    # Search (future)
    "search": "search",
    "find": "search",
    "lookup": "search",

}


def resolve(intent: str) -> str:
    """
    Converts different user words into one canonical intent.
    """

    return INTENT_ALIASES.get(
        intent.lower(),
        intent.lower()
    )
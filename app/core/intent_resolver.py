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



    "create": "create",
    "make": "create",
    "new": "create",
    
    
       
    "read": "read",
    "show": "read",
    "display": "read",
    "write": "write",
    "append": "append",
    "rename": "rename",
    "delete": "delete",
    "remove": "delete",
}



def resolve(intent: str) -> str:
    """
    Converts different user words into one canonical intent.
    """

    return INTENT_ALIASES.get(
        intent.lower(),
        intent.lower()
    )
"""
EGO

Entry point of the application.

Author: Syed
Version: 0.8.0-alpha
"""

from app.core.parser import Parser
from app.core.router import Router
from app.core.brain import Brain

from app.core.version import (
    NAME,
    FULL_NAME,
    VERSION,
    CODENAME,
    BUILD,
    AUTHOR,
)


def main():

    print("=" * 65)
    print(f"🤖 {FULL_NAME}")
    print("=" * 65)
    print(f"Version   : {VERSION}")
    print(f"Codename  : {CODENAME}")
    print(f"Build     : {BUILD}")
    print(f"Author    : {AUTHOR}")
    print("=" * 65)
    print("Type 'exit' to quit.")
    print("=" * 65)

    parser = Parser()
    router = Router()
    brain = Brain()

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        command = parser.parse(user_input)

        command = brain.think(command)

        response = router.route(command)

        if response:
            print(f"EGO: {response.message}")
        else:
            print("EGO: Sorry, I don't understand that command yet.")


if __name__ == "__main__":
    main()
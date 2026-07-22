"""
EGO

Entry point of the application.

Author: Syed
Version: 0.2.0-alpha
"""

from app.core.parser import Parser
from app.core.router import Router
from app.core.brain import Brain

def main():

    print("=" * 50)
    print("EGO Personal AI Assistant")
    print("Type 'exit' to quit.")
    print("=" * 50)

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
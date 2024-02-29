import os
from rich import print

# Clear terminal function
def clear():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix/Linux
        os.system('clear')


# Print feedback box at top of the CLI.
def feedback(user_input, feedback_type):
    if feedback_type == "error":
        print(f"[ Virheellinen syöte: [red]\"{user_input}\"[/red] ! ]")
    elif feedback_type == "none":
        print(f"[ {'~' * 24} ]")


# Clears screen and sets EMPTY feedback box.
def new():
    clear()
    option = False
    feedback(option, "none")


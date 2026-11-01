"""
Task 2 – Greeting Function with String Manipulation
---------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces at the start and end with .strip()
- capitalizes the first letter with .capitalize()
  (note: .capitalize() also makes the REST of the string lowercase)
- returns exactly: "Hello, <Name>! Welcome to Python!"
- if the name is empty (or only spaces), uses "Stranger" as the name

In the main block: ask the user for their name and print the greeting.

Example run:
    Enter your name:   alice
    Hello, Alice! Welcome to Python!

Examples (these are also used to check your work):
>>> greet_user("alice")
'Hello, Alice! Welcome to Python!'
>>> greet_user("   bob  ")
'Hello, Bob! Welcome to Python!'
>>> greet_user("anna MARIE")
'Hello, Anna marie! Welcome to Python!'
>>> greet_user("   ")
'Hello, Stranger! Welcome to Python!'
"""


def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    #removing whitespace
    clean_name = name.strip()

    #checking if the string is empty
    if clean_name == "":
        clean_name = "Stranger"
    else:
        #capitalizing the first letter and lowercasign the rest
        clean_name = clean_name.capitalize()
    return f"Hello, {clean_name}! Welcome to Python!"
    raise NotImplementedError("greet_user() is not implemented yet")


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    #example checks block
    print("--- Example checks ---")
    print(repr(greet_user("alice")))
    print(repr(greet_user("  bob  ")))
    print(repr(greet_user("anna MARIE")))
    print(repr(greet_user(" ")))
    print("----------------------\n")

    user_input = input("your name: ")
    greeting = greet_user(user_input)
    print(greeting)
    pass

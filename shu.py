import random

# Use a list for doors to keep things tidy
doors = ["door 1", "door 2", "door 3"]
user_choice = input("Choose your door (door 1, door 2, or door 3): ").lower()

statements = [
    "Congrats! You won a new car!",
    "A bucket of confetti falls on your head. Happy Tuesday!",
    "You open the door to find... a brick wall. How boring."
]

# This shuffles the list itself; it doesn't create a new variable
random.shuffle(statements)

if user_choice in doors:
    # We grab the first item from the now-shuffled list
    print(statements[0])
else:
    print("That's not a valid door! Try again.")
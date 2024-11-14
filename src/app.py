import random

# Constants
NUMBER_RANGE = (1, 100)
DIFFICULTY_LEVELS = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {NUMBER_RANGE[0]} and {NUMBER_RANGE[1]}.\n")

def get_difficulty_level():
    """Prompts the user to select a difficulty level and returns the number of chances."""
    print("Please select the difficulty level:")
    for i, level in enumerate(DIFFICULTY_LEVELS.keys(), 1):
        print(f"{i}. {level} ({DIFFICULTY_LEVELS[level]} chances)")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(DIFFICULTY_LEVELS):
                level = list(DIFFICULTY_LEVELS.keys())[choice - 1]
                return level, DIFFICULTY_LEVELS[level]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_guess():
    """Prompts the user to enter a guess and returns it as an integer."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Main game loop."""
    display_welcome_message()
    level, lives = get_difficulty_level()
    random_number = random.randint(*NUMBER_RANGE)
    attempts = 0

    print(f"\nGreat! You have selected the {level} difficulty level.\nLet's start the game!\n")

    while lives > 0:
        guess = get_user_guess()
        attempts += 1

        if guess > random_number:
            print(f"Incorrect! The number is less than {guess}\n")
        elif guess < random_number:
            print(f"Incorrect! The number is greater than {guess}\n")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.\n")
            return

        lives -= 1
        print(f"You have {lives} chances left.\n")

    print(f"Sorry, you've run out of chances. The correct number was {random_number}.\n")

if __name__ == "__main__":
    play_game()

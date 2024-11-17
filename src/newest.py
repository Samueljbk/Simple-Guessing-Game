import random

# Game configuration
MIN_NUMBER = 1
MAX_NUMBER = 100
DIFFICULTY_LEVELS = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}

def display_welcome_message():
    """Displays the welcome message and rules of the game."""
    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}")

def get_difficulty_level():
    """Prompts the user to select a difficulty level and returns the level name and chances."""
    print("\nPlease select the difficulty level:")
    for i, (level, chances) in enumerate(DIFFICULTY_LEVELS.items(), 1):
        print(f"{i}. {level} ({chances} chances)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if 1 <= choice <= len(DIFFICULTY_LEVELS):
                level = list(DIFFICULTY_LEVELS.keys())[choice - 1]
                return level, DIFFICULTY_LEVELS[level]
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_guess():
    """Gets and validates the user's guess."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
            print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Runs the main game loop."""
    display_welcome_message()
    level_name, chances = get_difficulty_level()
    
    print(f"\nGreat! You have selected {level_name} difficulty.")
    print("Let's start the game!")
    
    # Generate random number
    target_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    
    # Main game loop
    while chances > 0:
        print(f"\nYou have {chances} chances left.")
        guess = get_valid_guess()
        attempts += 1
        
        if guess == target_number:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            return True
        
        hint = "less" if guess > target_number else "greater"
        print(f"\nIncorrect! The number is {hint} than {guess}")
        chances -= 1
    
    print(f"\nGame Over! The number was {target_number}")
    return False

def main():
    """Main function to run the game and handle playing again."""
    while True:
        play_game()
        
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no', 'y', 'n']:
                break
            print("Please enter 'yes' or 'no'")
        
        if play_again in ['no', 'n']:
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
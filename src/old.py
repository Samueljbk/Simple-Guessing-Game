import random


def main():
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the coreect number.\n")

    print(f"Please select the difficulty level:")
    print(f"1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")

    difficulty_choice = int(input("Enter your choice: "))
    if difficulty_choice == 1:
        difficulty_choice = "Easy"
        lives = 10
    if difficulty_choice == 2:
        difficulty_choice = "Medium"
        lives = 5
    if difficulty_choice == 3:
        difficulty_choice = "Hard"
        lives = 3
    
    print(f"\nGreat! You have selected the {difficulty_choice} difficulty level.\nLet's start the game!\n")
    random_number = random.randint(1, 100)
    print(random_number)
    attempts = 1

    while lives > 0:
        guess = int(input("Enter your guess: "))
        if guess > random_number:
            print(f"Incorrect! The number is less than {guess}\n")
        if guess < random_number:
            print(f"Incorrect!: The number is greater than {guess}\n")
        if guess == random_number:
            print(f"Congarulations! You guessed the number in {attempts}")
            
        attempts += 1
        lives = lives - 1
    
main()
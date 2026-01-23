import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Enter your guess: ")
        
        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Start the game
number_guessing_game()
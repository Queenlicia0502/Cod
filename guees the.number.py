import random

print("Welcome to the Guess the Number Game!")

# The computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = input("Enter your guess (1–100): ")

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break

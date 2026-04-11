import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break
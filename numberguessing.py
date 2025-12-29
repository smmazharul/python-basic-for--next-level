import random as rnd

lowest = 1
highest = 6
number_to_guess = rnd.randint(lowest, highest)
number_of_attempts = 0

while True:
    user_input = int(input(f"Guess a number between {lowest} and {highest}:"))
    number_of_attempts += 1
    if user_input <lowest or user_input>highest:
        print(f"Please guess a number within the range of {lowest} to {highest}.")
        continue
    elif user_input > number_to_guess:
        print("Too high!")
    elif user_input < number_to_guess:
        print("Too low!")
    else:
        print("You guessed it!")
        break
print(f"You took {number_of_attempts} attempts to guess the number {number_to_guess}.")
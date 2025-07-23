# Guess the Number Game 

import random

def guess_the_number():
    number = random.randint(1,100)
    guess = 0
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")
    while guess != number:
        guess = int(input("Take a guess:"))
        attempts += 1
        if guess < number:
            print("Too low. Enter a higher number.")
        elif guess > number:
            print("Too high. Enter a lower number.")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")

def main_func():
    play_again = "yes"
    while play_again =="yes":
        guess_the_number()
        play_again = input("Do you want to play again? (yes/no):")
    print("Thank you for playing.")


main_func()
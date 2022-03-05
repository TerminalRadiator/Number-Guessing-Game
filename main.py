import random

num = random.randint(1, 10)
num_guessed = int(input("Welcome to the Number Guessing Game!!! Please guess a number: "))


while num_guessed != num:
    num_guessed = int(input("Guess again: "))

if num_guessed == num:
    print("You guessed correctly!!!")







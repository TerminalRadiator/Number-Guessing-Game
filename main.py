import random

chance = 7
num = random.randint(1, 101)
num_guessed = int(input("Welcome to the Number Guessing Game!!! Please guess a number: "))


while num_guessed != num and chance != 0:
    chance -= 1
    if chance == 0:
        print('You lose!!!')
    else:
        print(f"You have {chance} chances left")
        if num_guessed < num:
            print("The number is higher")
        else:
            print('The number is lower')
        num_guessed = int(input("Guess again: "))

if num_guessed == num:
    print("You guessed correctly!!!")







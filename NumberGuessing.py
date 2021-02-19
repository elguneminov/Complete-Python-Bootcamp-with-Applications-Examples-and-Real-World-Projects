""" Python Modules """
import random
import time
print('Welcome to the game!')

random_number = random.randint(1, 50)
guessing_chance = 10

while True:
    guessing_number = int(input('Enter your guess: '))
    if guessing_number < random_number:
        print('Please wait for result....')
        time.sleep(2)
        print('Your number is less than real number')
        guessing_chance -= 1
        print('Your guessing chance: ', guessing_chance)
    elif guessing_number > random_number:
        print('Please wait for result')
        time.sleep(2)
        print('Your number is grater than real number')
        guessing_chance -= 1
        print('Your guessing chance: ', guessing_chance)
    elif guessing_number == random_number:
        print('Please wait for result')
        time.sleep(2)
        print('Congrats!')
        break
    if guessing_chance == 0:
        print('You lost the game!')
        break

import random

player_number=int(input('Enter a number of your choice between 0 to 9: '))

system_number = random.randint(0,10)
if player_number == system_number:
    print('You won')
else:
    print('You lost')
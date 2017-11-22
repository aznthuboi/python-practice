import random

num = random.randint(1,10)
guess = 0
count = 0

while guess != num and guess != 'exit':
    guess = int(input("Pick a number from 1-9: "))

    if guess == 'exit':
        break

    count += 1

    if guess > num:
        print('too high')
    elif guess < num:
        print('too low')
    else:
        print('You guess right')
        print('Only took you ' , count , 'tries')


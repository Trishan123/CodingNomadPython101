# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
num = random.randint(1, 10)
guess = None
tries = 0
while guess != num and tries < 3:
    guess = int(input("guess a number between 1 and 10:"))
    tries += 1

    if guess == num:
        print("Congratulations! You won!")
    else:
        print("Nope sorry, try again!")
        if tries >= 3:
            print("Sorry you ran out of guess")
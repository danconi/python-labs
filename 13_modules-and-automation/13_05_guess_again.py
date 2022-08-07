# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
userinput = input("type a number: ")
number = random.randint(0, 10)

tries = 1
while number != int(userinput) :
    tries = tries + 1
    if tries > 3:
        print('you lost the game')
        break

    userinput = input("try again: ")
     

    

    
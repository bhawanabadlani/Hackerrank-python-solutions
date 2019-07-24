######################Guessing Game#####################
 
import random 
random_int = random.randint(0,9)
i = 1;
while i<=3:
    user_guess = int(input(f"Guess {i}: "))
    if user_guess == random_int:
        print('Congratulations!! \nYou Won! :) ')
        break
        exit()
    elif i==3 :
        print(f"Sorry, You Loose :( \n The number is {random_int} ")
    else:
        i += 1


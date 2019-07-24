######################Guessing Game#####################
 
import random 
secret_number = random.randint(0,9)
guess_limit = 3
guess_count = 1
while guess_count<=guess_limit:
    guess = int(input(f"Guess {guess_count}: "))
    guess_count += 1
    if guess == secret_number:
        print('Congratulations!! \nYou Won! :) ')
        break
else :
    print(f"Sorry, You Loose :( \nThe number is {secret_number} ")



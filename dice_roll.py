import random

while True:
    userChoice = input ("Roll the dice? (y/n) : " .lower() )

    if userChoice == 'y' :
     die1 = random.randint(1, 6)
     print(f'({die1})')

    elif userChoice == "n" :
     print("Thanks for playing!!")
     break

    else:
     print("Invaild choice")    
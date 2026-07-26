import random

guessing_number = random.randint(1, 100)
while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))
        if user_guess < guessing_number:
            print("Too low")
        elif user_guess > guessing_number:
            print("Too high")
        else:
            print("Congratulation!! GUESSED RIGHT ")  
            break          
    except ValueError:
        print("Please entre a vaild number")



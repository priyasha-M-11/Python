import random

emojis = {"r" : "🪨", "s" : "✂️", "p" : "📃"}# dictionary to store key-value pairs "p" will go with "paper emoji"
choices = ('r', 'p', 's')# tuple to store choices, so can not be modified

user_name = input("Enter your name: ")#get user's name


while True: #loop until user wants to exit

    user_choice = input("Rock, paper, or scisssors? (r/p/s)").lower() #User's choice on what to play
    if user_choice not in choices:
        print ("Invaild choice")# error-handlign for characters not in choices
        continue #to start from the start of the loop again

    computer_choice = random.choice(choices)# for the comouter choice, random select from choices tuple

    #printing what user and computer chose with emojis from key-value pair
    print(f" {user_name} chose : {emojis[user_choice]} ") #inculding user's name to make it more personal
    print(f" Computer chose : {emojis[computer_choice]} ")

    if user_choice == computer_choice:
        print("Tie!") # if both chose the same
    elif ((user_choice == "r" and computer_choice =="s") or #conditions for user winning in an if statment, else will be computer winning
        ( user_choice == "s" and computer_choice =="p") or 
        ( user_choice == "p" and computer_choice =="r")):
        print(f" {user_name} Wins!") #user wins
    else:
        print(f"{user_name} loses :( ") #user loses

    user_exit = input("Exit game? (y/n): ")# check if user wants to continue playing

    if user_exit == "y":# if user enter "y" will break out of loop and program will end 
        break


    
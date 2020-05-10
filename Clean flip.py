import random

win_counter = 0
loss_counter = 0

coin_flip = True

while coin_flip == True:
    outcome = random.randint(1,101)
    #even numbers are heads
    #odd numbers are tails

#define user inputs
    user_choice = input("Choose Heads or Tails: ")
    if user_choice in ["Heads", "heads", "head", "Head"]:
        user_choice = "heads"
    elif user_choice in ["Tails", "tails", "tail", "Tail"]:
        user_choice = "tails"
    else:
        print("Something wrong, I can feel it")
#end of user inputs



#input is Heads and outcome is heads
    if user_choice == "heads" and outcome % 2 == 0:
        print("The result was Heads, You Win ")
        win_counter += 1
        print("Number of wins: " + str(win_counter))
        try_again = input("Do you want to try again?  Yes/No : ")

#inupt is heads and outcome is tails
    elif user_choice == "tails" and outcome % 2 != 0:
        print("The result was Tails, You Win")
        win_counter += 1
        print(win_counter)
        try_again = input("Do you want to try again?  Yes/No : ")

#input is heads and outcome is tails
    elif  user_choice == "heads" and outcome % 2 != 0:
        print("The result was Tails, You Lose")
        loss_counter += 1
        print("Number of losses: " + str(loss_counter))
        try_again = input("Do you want to try again?  Yes/No : ")

#input is tails and outcome is heads
    elif  user_choice == "tails" and outcome % 2 == 0:
        print("The result was Heads, You Lose")
        loss_counter += 1
        print("Number of wins: " + str(win_counter))
        try_again = input("Do you want to try again?  Yes/No : ")

    else:
        print("code does not work")
        try_again = input("Do you want to try again?  Yes/No : ")


    if try_again in ["yes", "Yes", "y", "Y"]:
        pass
    else:
        print("Goodbye")
        break



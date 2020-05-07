###----------CODE-DO-NOT-EDIT---------------------#####
def flip_coin(input):

    import random
    random_list = [random.randint(1,101) for i in range(101)]
    random_num = random.choice(random_list)
    if input == "heads" or input == "Heads":
        if random_num % 2 == 0:
            print("The result was Heads, You Win")
            return True
        else:
            print("It was Tails, You Lose")
            return False

    elif input == "Tails" or input == "tails":
        if random_num % 2 != 0:
            print("The result was Tails, You Win")
            return True

        elif random_num % 2 == 0:
            print("It was Heads, You Lose")
            return False


###----------END-OF-MAIN-CODE---------------------#####
###-----------------Counter-Code------------------####


#Enter Heads or Tails in the function below
flip_coin("Heads")


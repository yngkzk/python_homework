import random

def get_random_int(min, max):
    result = random.random() * (max - min)
    result += min
    return int(result)

def game(my_random, min, max, attempts=7):
    user_in = input("Guess the number from %s to %s. Remaining attempts - %s : " % (min, max, attempts))
    try:
        user_num = int(user_in)
    except ValueError:
        print("Enter integer only!")
        game(my_random, min, max, attempts-1)
    else:
        if attempts == 0:
            print("No more attempts.")
            return
        elif my_random > user_num:
            print("More.")
            game(my_random, min, max, attempts-1)
        elif my_random < user_num:
            print("Less.")
            game(my_random, min, max, attempts-1)
        else:
            print("Correct, %d! Remaining attempts - %s!" % (my_random, attempts))
            return

num = get_random_int(0, 20)
game(num, 0, 20)
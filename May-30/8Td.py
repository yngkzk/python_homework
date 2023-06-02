print("This is a multiple choice test. Write your answer in one letter.")
user_test_1 = input("1. How many sides does a triangle have? a) 1 b) 2 c) 3 : ")
user_test_2 = input("2. What is the periemeter of a square if its side is 2? a) 4 b) 8 c) 16 : ")
user_test_3 = input("3. what is the sum of the interior angles of a triangle? a) 360 b) 180 c) 90 : ")
score = 0
try:
    t1 = str(user_test_1)
    t2 = str(user_test_2)
    t3 = str(user_test_3)
except ValueError:
    msg = "Incorrect data. You have to enter numbers!"
except NameError as Nerr:
    msg = "Incorrect data.", Nerr
if user_test_1 == int(user_test_1) or user_test_2 == int(user_test_2):
    print("Incorrect data. You have to enter a letter!")
elif user_test_3 == int(user_test_3):
    print("Incorrect data. You have to enter a letter!")
elif t1 == "c":
    score += 2
elif t2 == "b":
    score += 2
elif t3 == "b":
    score += 2
else:
    print("Result.")
print("Your score: ", score)

print("This is a multiple choice test. Write your answer in numbers.")
user_test_1 = input("1. How many sides does a triangle have? a) 1 b) 2 c) 3 : ")
user_test_2 = input("2. What is the periemeter of a square if its side is 2? a) 4 b) 8 c) 16 : ")
user_test_3 = input("3. what is the sum of the interior angles of a triangle? a) 360 b) 180 c) 90 : ")

score = 0

try:
    user_test_1 = int(user_test_1)
    user_test_2 = int(user_test_2)
    user_test_3 = int(user_test_3)
except ValueError:
    msg = "Incorrect data. You have to enter numbers!"
else:
    if user_test_1 == 3:
        score += 2
    if user_test_2 == 8:
        score += 2
    if user_test_3 == 180:
        score += 2
    else:
        print("Result.")
print("Your score: ", score)

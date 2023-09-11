from random import randint

N = 6
M = 8
A = []
B = []
for i in range(N):
    for x in range(M):
        B.append(randint(-10, 10))
    A.append(B)
    B = []

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

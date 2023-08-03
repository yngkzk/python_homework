from random import randint

N = 3
M = 3
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

summary = 0
for z in range(len(A)):
    for y in range(len(A[z])):
        if A[z][y] % 2:
            summary += A[z][y]
        else:
            continue
print(summary)


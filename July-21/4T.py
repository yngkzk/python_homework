from random import randint

N = 3
M = 5
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


for z in range(len(A)):
    max_number = None
    for y in range(len(A[z])):
        if max_number is None or A[z][y] > max_number:
            max_number = A[z][y]
    print(max_number, f'max number in {z+1} horizontal line \n')

print('\n')
for u in range(M):
    max_number = None
    for y in range(len(A)):
        if max_number is None or A[y][u] > max_number:
            max_number = A[y][u]
    print(max_number, f'max number in {u + 1} vertical line \n')

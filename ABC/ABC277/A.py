A = [1, 2, 3]
B = []


for _ in range(3):
    B.append(A)

print(B)

B[0][0] = 100

print(B)
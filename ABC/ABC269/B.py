S = []

for _ in range(10):
    S.append(list(input()))

A = None

for i in range(10):
    for j in range(10):
        if S[i][j] == "#" and A == None:
            A = i+1
            C = j+1


B = 0
D = 0
for i2 in range(10-A+1):
    for j2 in range(10-C+1):
        if S[A+i2-1][C+j2-1] == "#":
            B = max(B, A+i2)
            D = max(D, C+j2)

print(A,B)
print(C, D)
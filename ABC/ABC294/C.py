N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()

A.append(-1)
B.append(-1)

aLastIndex = 0
bLastIndex = 0

resA = []
resB = []

for i in range(len(C)):
    aLast = A[aLastIndex]
    bLast = B[bLastIndex]

    if C[i] == aLast:
        resA.append(i+1)
        aLastIndex += 1
    elif C[i] == bLast:
        resB.append(i+1)
        bLastIndex += 1

print(*resA)
print(*resB)

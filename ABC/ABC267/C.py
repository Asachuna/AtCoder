import numpy as np

N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))

mask = np.arange(1, M+1)
curSum = sum(A[0:M] * mask)
curArrSum = np.sum(A[1:M])
max = curSum

for i in range(N-M):
    if max < curSum:
        max = curSum

    diff = M * A[i+M] - curArrSum - A[i]

    curSum += diff

    curArrSum -= A[i+1]
    curArrSum += A[i+M]

        

if max < curSum:
    max = curSum

print(max)
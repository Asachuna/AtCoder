import numpy as np

H, W, N, h, w = map(int, input().split())
A = []

for _ in range(H):
    arr = list(map(int, input().split()))
    A.append(arr)

A = np.array(A)

def checkNum(W, H):
    target = A[0:H+1, 0:W+1]

    uq, cnt = np.unique(target, return_counts=True)

    return uq, cnt

#累積和
acc = np.zeros((N, H, W), dtype=int)

uq, c = checkNum(W, H)
uniqueNumCount = len(uq)

for x in range(W):
    for y in range(H):
        uq, cnt = checkNum(x, y)

        for i in range(len(uq)):
            num = uq[i] - 1
            acc[num, y, x] = cnt[i]

w -= 1
h -= 1

for y in range(H-h):
    arr = []
    for x in range(W-w):
        count = 0
        for num in range(N):
            result = acc[num, y+h, x+w]

            if (x > 0):
                result -= acc[num, y+h, x-1]
            if (y > 0):
                result -= acc[num, y-1, x+w]
            if (x>0 and y>0):
                result += acc[num, y-1, x-1]
            
            if result == acc[num, H-1, W-1]:
                count += 1
        arr.append(uniqueNumCount - count)


    print(*arr)



import sys
sys.setrecursionlimit(1000000000)

N, M = map(int, input().split())

A = list(map(int, input().split()))

B = list(range(1, N+1))

#k回目の操作でxに居る
dp = [{} for k in range(M)]

index = 0
hashigo = []

for k in range(M):

    a = A[k]

    t1 = B[a-1]
    t2 = B[a]

    if t1 == 1:
        index = a
    elif t2 == 1:
        index = a-1

    B[a-1], B[a] = B[a], B[a-1]
    hashigo.append(index)

def next(k, x):
    if k >= M:
        return x+1

    if x in dp[k]:
        return dp[k][x]

    a = A[k]
    if a == x or a-1 == x:
        t = None
        if a == x:
            t = a-1
        else:
            t = a

        res = next(k+1, t)
        dp[k][x] = res
        return res

    else:
        res = next(k+1, x)
        dp[k][x] = res
        return res

result = []

for i in range(M):
    i = M-i-1


    startPos = hashigo[i-1]
    if i == 0:
        startPos = 0

    ans = next(i+1, startPos)
    result.append(ans)

for i in range(M):
    print(result[M-i-1])
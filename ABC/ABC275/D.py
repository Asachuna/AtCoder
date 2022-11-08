import sys
sys.setrecursionlimit(10 ** 8)

import math
N = int(input())

dp = {}

def func(i):
    if i == 0:
        return 1

    a = math.floor(i/2)
    b = math.floor(i/3)

    if a not in dp:
        dp[a] = func(a)
    if b not in dp:
        dp[b] = func(b)
    aAns = dp[a]
    bAns = dp[b]

    return aAns + bAns

print(func(N))

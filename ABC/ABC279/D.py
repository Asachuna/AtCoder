import math
A, B = map(int, input().split())

def falltime(g):
    return A / math.sqrt(g)

zeroT = (A / B / 2) ** (2 / 3)
zeroT = math.floor(zeroT)
print(falltime(1+zeroT) + zeroT * B)
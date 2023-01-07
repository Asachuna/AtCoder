D = int(input())

N = int(input())

sums = [0] * (D+1)

for _ in range(N):
    L, R = map(int, input().split())
    sums[L-1] += 1
    sums[R] -= 1

current = 0

for i in range(D):
    current += sums[i]
    print(current)
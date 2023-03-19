N = int(input())

A = list(map(int, input().split()))

res = []

for a in A:
    if a%2 == 0:
        res.append(a)

print(*res)
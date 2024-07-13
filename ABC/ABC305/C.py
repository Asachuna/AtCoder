N = int(input())
A = list(map(int, input().split()))

count = {}
for i in range(1, N+1):
    count[i] = 0

result = []

for a in A:
    count[a] += 1
    if count[a] == 2:
        result.append(str(a))

print(" ".join(result))
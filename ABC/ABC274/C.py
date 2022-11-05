N = int(input())
A = list(map(int, input().split()))

result = [0]

for i in range(N):
    a = A[i]
    parentIndex = a-1
    result.append(result[parentIndex]+1)
    result.append(result[parentIndex]+1)

for r in result:
    print(r)


N, K = map(int, input().split())
A = list(input().split())

for _ in range(K):
    A.pop(0)
    A.append(0)

A = list(map(str, A))

print(" ".join(A))
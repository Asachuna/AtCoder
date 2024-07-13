N = int(input())
A = list(map(int, input().split()))


Q = int(input())

Asum = [0]
current = 0
for i in range(1, N):
    if (i%2 == 0):
        current += A[i] - A[i-1]
    
    Asum.append(current)

print(Asum)
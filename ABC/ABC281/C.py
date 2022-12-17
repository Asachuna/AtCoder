N, T = map(int, input().split())

A = list(map(int, input().split()))

sum = sum(A)

T = T%sum

time = 0
prevTime = 0

result = None

for i in range(N):
    time += A[i]
    if time > T:
        result = i+1, T - prevTime
        break
    prevTime = time

print(*result)

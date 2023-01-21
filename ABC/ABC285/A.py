N, a, b, c, d = map(int, input().split())

a = a-1
b = b
c = c-1
d = d

A = list(map(int, input().split()))

t1 = A[:a]
t2 = A[a:b]
t25 = A[b:c]
t3 = A[c:d]
t4 = A[d:]


result = []

result.extend(t1)
result.extend(t3)
result.extend(t25)
result.extend(t2)
result.extend(t4)

print(*result)
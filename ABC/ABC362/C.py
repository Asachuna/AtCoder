N = int(input())
L = []
R = []

for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

X = [(L[i] + R[i]) // 2 for i in range(N)]

total = sum(X)
adjustment = -total

for i in range(N):
    if adjustment > 0:
        add = min(R[i] - X[i], adjustment)
        X[i] += add
        adjustment -= add
    elif adjustment < 0:
        sub = min(X[i] - L[i], -adjustment)
        X[i] -= sub
        adjustment += sub

    if adjustment == 0:
        break

if adjustment == 0:
    print("Yes")
    print(*X) 
else:
    print("No")
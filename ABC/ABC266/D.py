N = int(input())
Tdiff = []
Xdiff = []
A = []

Tprev = 0
Xprev = 0

for _ in range(N):
    t, x, a = map(int, input().split())
    A.append(a)

    if Tprev != None:
        td = t - Tprev
        xd = x - Xprev
        Tdiff.append(td)
        Xdiff.append(xd)

    Tprev = t
    Xprev = x


def getDiff(i):
    return Tdiff[i] - abs(Xdiff[i])

point = 0

for i in range(N-1):
    if getDiff(i) >= 0:
        point += A[i]

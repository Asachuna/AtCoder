N, lastX, lastY = map(int, input().split())
A = list(map(int, input().split()))

#水平移動
hor = []
#垂直移動
ver = []

hor = A[0::2]
ver = A[1::2]

first = hor[0]
hor = hor[1:]

hor.sort()
ver.sort()
hor.reverse()
ver.reverse()

x, y = first, 0

for v in ver:
    if y <= lastY:
        y += v
    else:
        y -= v

for h in hor:
    if x <= lastX:
        x += h
    else:
        x -= h

if x == lastX and y == lastY:
    print("Yes")
else:
    print("No")
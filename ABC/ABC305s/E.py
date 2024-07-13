s = [[""] * 40 for _ in range(40)]

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = 0
y = 0
cur = 0
it = 0

for i in range(1600):
    dx = dirs[cur][0]
    dy = dirs[cur][1]

    if x+dx>=40 or y+dy>=40 or y+dy<0 or x+dx<0 or s[y+dy][x+dx] != "":
        cur += 1
        if cur >= 4:
            cur = 0

    dx = dirs[cur][0]
    dy = dirs[cur][1]

    s[y][x] = abc[it]
    print(x, y, dx, dy)

    x += dx
    y += dy
    it += 1

    if it >= 26:
        it = 0

sr = ""
for i in range(40):
    sr += s[i][i]
print(sr)
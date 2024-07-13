H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

minx = 99999
maxx = -1
miny = 99999
maxy = -1

for x in range(W):
    for y in range(H):
        if S[y][x] == "#":
            if x < minx:
                minx = x
            if y < miny:
                miny = y
    
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        if S[y][x] == ".":
            print(x+1,y+1)

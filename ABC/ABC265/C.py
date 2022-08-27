H, W = map(int, input().split())
G = []
for _ in range(H):
    G.append(list(input()))

x,y = 0,0
flag = False

for _ in range(H*W+1):
    s = G[y][x]


    if s == "U":
        if y <= 0:
            flag = True
            break
        else:
            y -= 1
    
    if s == "D":
        if y >= H-1:
            flag = True
            break
        else:
            y += 1

    if s == "L":
        if x <= 0:
            flag = True
            break
        else:
            x -= 1
    
    if s == "R":
        if x >= W-1:
            flag = True
            break
        else:
            x += 1


if flag:
    print(y+1, x+1)
else:
    print(-1)
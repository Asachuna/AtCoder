alps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

H, W = map(int, input().split())
res = [[0]*W for _ in range(H)]

inputs = [list(map(int, input().split())) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if inputs[y][x] == 0:
            res[y][x] = "."
        else:
            res[y][x] = alps[inputs[y][x]-1]

for r in res:
    print("".join(r))

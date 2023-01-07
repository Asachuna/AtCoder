H, W = map(int, input().split())

ver_sum = []

for _ in range(H):
    row = list(map(int, input().split()))
    res = []
    cur = 0

    for i in range(W):
        cur += row[i]
        res.append(cur)
    ver_sum.append(res)

csum2d = [ver_sum[0]]

import numpy as np


for y in range(1, H):
    csum2d.append([])
    for x in range(W):
        csum2d[y].append(csum2d[y-1][x] + ver_sum[y][x])



Q = int(input())

for q in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    b1 = csum2d[y2-1][x2-1]
    b2, b3, b4 = 0, 0, 0

    if y1 != 1:
        b3 = csum2d[y1-2][x2-1]
    
    if x1 != 1:
        b4 = csum2d[y2-1][x1-2]

    if x1 != 1 and y1 != 1:
        b2 = csum2d[y1-2][x1-2]
    
    print(b1+b2-b3-b4)

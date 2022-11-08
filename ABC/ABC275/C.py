S = []
import itertools

for _ in range(9):
    S.append(list(input()))

count = 0

def point2xy(p):
    #x, y
    return p%9, p//9

def beclong(bec):
    return bec[0]**2 + bec[1]**2

def becChokko(bec1, bec2):
    return bec1[0]*bec2[0] + bec1[1]*bec2[1] == 0

a = list(range(81))

for comb in itertools.combinations(a, 3):
    x1, y1 = point2xy(comb[0])
    x2, y2 = point2xy(comb[1])
    x3, y3 = point2xy(comb[2])


    if [x1, y1] != [x2, y2] and [x1, y1] != [x3, y3] and [x3, y3] != [x2, y2]:
        if S[y1][x1] == "#" and S[y2][x2] == "#" and S[y3][x3] == "#":
            bect2 = [x2-x1, y2-y1]
            bect3 = [x3-x1, y3-y1]

            if beclong(bect2) != beclong(bect3) or not becChokko(bect2, bect3): continue

            bect = [bect2[0]+bect3[0], bect2[1]+bect3[1]]

            ya = y1+bect[1]
            xa = x1+bect[0]

            if 0 <= xa and xa <= 8 and 0 <= ya and ya <= 8:
                if S[ya][xa] == "#":
                    count += 1

print(count)
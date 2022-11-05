H, W, r, c = map(int, input().split())

maps = []
for _ in range(H+1):
    maps.append([0] * (W+1))

N = int(input())

for _ in range(N):
    ra, ca = map(int, input().split())
    maps[ra-1][ca-1] = 1

Q = int(input())

result = []

for i in range(Q):
    d, l = map(str, input().split())
    l = int(l)

    for _ in range(l):
        test = [c, r]

        if d == "D":
            test[1] += 1
        elif d == "U":
            test[1] -= 1
        elif d == "R":
            test[0] += 1
        elif d == "L":
            test[0] -= 1

        if test[0] < 1 or test[1] < 1 or test[0] > W or test[1] > H or (maps[test[1]-1][test[0]-1]) == 1:
            break
        else:
            c = test[0]
            r = test[1]


    result.append([r, c])

for i in range(Q):
    print(result[i][0], result[i][1])
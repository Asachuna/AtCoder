N = int(input())
plus = list(map(int, input().split()))
Q = int(input())

base = 0
reset = False

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        reset = True
        x = query[1]
        plus = {}
        base = x

    if query[0] == 2:
        i, x = query[1]-1, query[2]
        if not reset:
            plus[i] += x
        elif str(i) in plus:
            plus[str(i)] += x
        else:
            plus[str(i)] = x

    if query[0] == 3:
        i = query[1]-1

        if not reset:
            print(plus[i])
        else:
            if str(i) in plus:
                print(plus[str(i)] + base)
            else:
                print(base)

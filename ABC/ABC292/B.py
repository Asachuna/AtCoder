N, Q = map(int, input().split())

p = [0] * N

for i in range(Q):
    q, pl = map(int, input().split())
    if q == 1:
        p[pl-1] += 1
    elif q == 2:
        p[pl-1] += 2
    
    elif q == 3:
        if p[pl-1] >= 2:
            print("Yes")
        else:
            print("No")
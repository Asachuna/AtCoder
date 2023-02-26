N, M = map(int, input().split())

S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

count = 0
for s in S:
    flag = False

    for t in T:
        if s.endswith(t):
            flag = True
            break
    
    if flag:
        count += 1

print(count)
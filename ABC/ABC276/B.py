N, M = map(int, input().split())

roads = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    roads[A-1].append(B)
    roads[B-1].append(A)

for i in range(N):
    c = roads[i]
    c.sort()

    print(str(len(c)) + " " +  " ".join(map(str, c)))
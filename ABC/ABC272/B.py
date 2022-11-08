N, M = map(int, input().split())

friends = []

for _ in range(N):
    friends.append([])

for cnt in range(M):
    k = list(input().split())
    k.pop(0)

    for i in k:
        for p in k:
            if i not in friends[int(p)-1]:
                friends[int(p)-1].append(i)

flag = True

for p in friends:
    if len(p) != N:
        flag = False

print(friends)

if flag:
    print("Yes")

else:
    print("No")
        




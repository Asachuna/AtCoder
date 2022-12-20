import numpy as np

H, W = map(int, input().split())

Sa = []

S = {}
for i in range(H):
    Sa.append(list(input()))

Sa = np.array(Sa)

for i in range(W):
    key = "".join(Sa[:, i])
    if key in S:
        S[key] += 1
    else:
        S[key] = 1


flag = True

Ta = []
for i in range(H):
    Ta.append(list(input()))

Ta = np.array(Ta)

for i in range(W):
    key = "".join(Ta[:, i])
    if key in S:
        if S[key] > 0:
            S[key] -= 1
        else:
            flag = False
            break
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
S = input()

res = -2

for i in range(len(S)):
    if S[i] == "a":
        res = i

print(res+1)
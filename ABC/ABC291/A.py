S = input()

result = 0

for i in range(len(S)):
    if "A" <= S[i] and S[i] <= "Z":
        result = i+1

print(result)
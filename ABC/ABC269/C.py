from itertools import combinations

N = int(input())

nb = list(format(N, 'b'))

ones = []

for i in range(len(nb)):
    if nb[i] == "1":
        ones.append(i)

result = []

for k in range(len(ones)+1):
    for comb in combinations(ones, k):
        x = ["0"]*len(nb)
        for c in comb:
            x[c] = "1"
        
        x = int("0b" + "".join(x), 2)
        result.append(x)

result.sort()

for r in result:
    print(r)
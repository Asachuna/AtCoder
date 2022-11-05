


H, W = map(int, input().split())

c = []
for _ in range(H):
    c.append(list(input()))

result = []

for j in range(W):
    count = 0
    for i in range(H):
        if c[i][j] == "#":
            count += 1
    
    result.append(str(count))

print(" ".join(result))
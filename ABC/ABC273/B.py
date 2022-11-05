x, k = map(int, input().split())

length = len(str(x))-1

for i in range(k):
    old = x

    if i > length:
        x = 0
        break

    target = int(str(x)[length-i])

    if target >= 5:
        x += 10 ** (i+1)
    
    
print(x)
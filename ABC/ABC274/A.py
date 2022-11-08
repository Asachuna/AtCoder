A, B = map(int, input().split())

a = str(round(B/A, 3))

for i in range(5-len(a)):
    a += "0"

print(a)

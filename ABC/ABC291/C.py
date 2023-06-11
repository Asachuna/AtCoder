N = int(input())
S = list(input())

s = set()
x = 0
y = 0

s.add("0,0")

flag = False

for i in range(N):
    if S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1
    elif S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    
    place = str(x)+","+str(y)

    if place in s:
        flag = True
        break

    s.add(place)
    

if flag:
    print("Yes")
else:
    print("No")


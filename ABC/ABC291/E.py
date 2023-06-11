N, M = map(int, input().split())

uppers = [set() for _ in range(N)]
downers = [set() for _ in range(N)]

def getNext(i, count):
    flag = False

    if count == N-1:
        return True

    for up in uppers[i]:
        result = getNext(up, count+1)

        if result == True:
            flag = True
            break
        else:
            uppers[i].remove(up)
    
    return flag


for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1

    uppers[x].add(y)
    downers[y].add(x)

result = False

target = -1

for i in range(M):
    if len(downers[i]) == 0:
        result = getNext(i, 0)
        target = i
        break


def getArr(i, arr):
    if (len(uppers[i])) != 0:
        for t in uppers[i]:
            arr.append(t)
            getArr(t, arr)

    return arr


if result:
    r = getArr(target, [target])

print(uppers)

print(result)
print(r)
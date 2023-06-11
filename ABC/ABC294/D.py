N, M = map(int, input().split())
from collections import deque


called = 0
callList = deque()
indexList = deque()


def is_ok(i, target):
    return callList[i] < target

def bisect(ng, ok, target):
    while (abs(ok-ng) > 1):
        mid = (ok+ng) // 2

        if is_ok(mid, target):
            ok = mid
        else:
            ng = mid
    
    return ng

memo = None

for _ in range(M):
    q = list(map(int,input().split()))
    
    if q[0] == 1:
        called += 1
        callList.append(called)
    if q[0] == 2:
        target = q[1]

        if target == callList[0]:
            callList.popleft()
            while len(callList) != 0 and callList[0] == -1:
                callList.popleft()
        else:
            index = bisect(len(callList)-1, 0, target)
            if index == 0:
                callList.popleft()

                while len(callList) != 0 and callList[0] == -1:
                    callList.popleft()

            else:
                callList[index] = -1


    if q[0] == 3:
        print(callList[0])
    




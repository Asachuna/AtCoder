import sys
import numpy as np
sys.setrecursionlimit(99999999)

N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))
A = np.flip(A)
dp = np.zeros(N)

def findMax(index):
    if dp[index] == 0:
        dp[index] = np.argmax(A[index:])
    return dp[index]
    
def findNext(sum, lastIndex, gen):
    print(gen)
    if gen == M:
        result.append(sum)
        return True
    
    maxIndex = int(findMax(lastIndex))

    if maxIndex == M-1:
        return
    else:
        maxNum = A[maxIndex]
        sum += maxNum * (M-gen)


result = []
findNext(0, -1, 1)
print(result)

print(max(result))


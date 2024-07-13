N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

maxdiff = A[len(A)-1] - A[0]


for i in range(K+1):
    diff = A[len(A)-1-(K-i)] - A[i]
    if (diff < maxdiff):
      maxdiff = diff
    

print(maxdiff)
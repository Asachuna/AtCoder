N, M, T = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)
R = [0] * (N)

for _ in range(M):
    x, y = map(int, input().split())
    R[x-1] = y

flag = True

for i in range(N):
    T -= A[i]

    if T <= 0:
        flag = False
        break
    
    T += R[i]



if flag:
    print("Yes")
else:
    print("No")
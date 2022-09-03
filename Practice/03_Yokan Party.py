N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
Adiff = [A[i+1] - A[i] for i in range(N-1)]
Adiff.append(L - A[len(A)-1])
Adiff.insert(0, A[0])

def is_ok(m):
    current = 0
    count = 0
    for i in range(N+1):
        current += Adiff[i]
        if current >= m:
            current = 0
            count += 1
    return count > K

def Mbisect(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return ok

print(Mbisect(0, L+1))
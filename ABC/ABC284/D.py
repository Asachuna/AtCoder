T = int(input())

def is_ok(x, N):
    return x**2 < N

def bisect(ng, ok, N):
    while (abs(ok-ng) > 1):
        mid = (ok+ng) // 2

        if is_ok(mid, N):
            ok = mid
        else:
            ng = mid
    
    return ok

def fact(n, b):
    na = n // b
    end = int(bisect(na, b, na))

    for p in range(2, end + 1):
        if n%(p**2) == 0:
            return p

border = 10**7

for t in range(T):
    N = int(input())

    flag = False

    #q(またはp)を全探索
    for p in range(2, min(border, N)):
        if N%p == 0:
            flag = True
            if N%(p**2) == 0:
                q = N//(p**2)
                print(p, q)
                break
            else:
                q = p
                p = bisect(N//q, 2, N//q)
                print(p+1, q)
                break
    
    #pを全探索
    if not flag:
        p = fact(N, border)
        q = N // (p**2)
        print(p, q)

    

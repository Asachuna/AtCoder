A, B, X = map(int, input().split())

def is_ok(x):
    return A * x + B * len(str(x)) <= X

def bisect(ng, ok):
    while (abs(ok-ng) > 1):
        mid = (ok+ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    
    return ok

print(bisect(10**9+1, 0))
N = int(input())

def is_ok(ok, mid):
    if direction == "row":
        A = 1
        B = N
        C = ok
        D = mid
    else:
        A = ok
        B = mid
        C = 1
        D = N
    
    q = ["?", str(A), str(B), str(C), str(D)]
    print(" ".join(q))

    ans = int(input())
    return ans != mid-ok+1

def bisect(ng, ok):
    while (abs(ok-ng) != 0):
        mid = (ok+ng) // 2
        if mid-ok==1:
            if is_ok(ok, ok):
                return ok
            else:
                return ng

        if is_ok(ok, mid):
            ng = mid
            lastng = False
        else:
            ok = mid
            lastng = True
    
    if (lastng):
        return ng
    else:
        return ok

direction = "row"
row = bisect(N, 1)

direction = "col"
col = bisect(N, 1)

print("!", row, col)
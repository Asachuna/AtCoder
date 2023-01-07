H, M = map(int, input().split())

def judge(H, M):
    H = f'{H:02}'
    M = f'{M:02}'
    mjH = H[0]+M[0]
    mjM = H[1]+M[1]
    
    return int(mjH) <= 23 and int(mjM) <= 59

r = None

while True:
    if judge(H, M):
        r = [H, M]
        break

    else:
        M += 1
        if (M == 60):
            M = 0
            H += 1
            if (H == 24):
                H = 0

print(r[0], r[1])
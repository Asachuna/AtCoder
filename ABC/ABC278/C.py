N, Q = map(int, input().split())

follows = {}

for i in range(Q):
    T, A, B = map(int, input().split())

    if (T == 1):
        follows[str(A)+"-"+str(B)] = True
    if (T == 2):
        follows[str(A)+"-"+str(B)] = False
    if (T == 3):
        if (str(A)+"-"+str(B)) in follows and (str(B)+"-"+str(A)) in follows and follows[str(A)+"-"+str(B)] == True and follows[str(B)+"-"+str(A)] == True:
            print("Yes")
        else:
            print("No")
    
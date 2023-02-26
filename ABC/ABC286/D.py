S = list(input())
T = list(input())

N = len(S)
Tlen = len(T)

stlist = [0] * (len(T))
enlist = [0] * (len(T))

for i in range(len(T)):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        stlist[i] = 1
    else:
        break

for i in range(len(T)):
    if S[N-i-1] == T[Tlen-i-1] or S[N-i-1] == "?" or T[Tlen-i-1] == "?":
        enlist[i] = 1
    else:
        break


for x in range(Tlen+1):
    st = False
    en = False

    if x == 0:
        st = True
    elif stlist[x-1] == 1:
        st = True

    if x == Tlen:
        en = True
    elif enlist[Tlen-x-1] == 1:
        en = True

    if st and en:
        print("Yes")
    else:
        print("No")
    
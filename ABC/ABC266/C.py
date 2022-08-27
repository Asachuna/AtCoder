a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

arr = [[a,b,c], [b,c,d], [c,d,a], [d,a,b]]
arr2 = [d, a, b, c]

def vec(a, b):
    return (a[0] - b[0], a[1] - b[1])

def tri_in(a, b, c, p): 

    ab = vec(b, a);
    bp = vec(p, b);

    bc = vec(c, b);
    cp = vec(p, c);

    ca = vec(a, c);
    ap = vec(p, a);

    #外積を求める
    c1 = ab[0] * bp[1]  - ab[1] * bp[0]
    c2 = bc[0] * cp[1]  - bc[1] * cp[0]
    c3 = ca[0] * ap[1]  - ca[1] * ap[0]

    return (c1 >= 0 and c2 >= 0 and c3 >= 0)or(c1 <= 0 and c2 <= 0 and c3 <= 0)


flag = True

for i in range(4):
    tri = arr[i]
    point = arr2[i]



    if tri_in(tri[0], tri[1], tri[2], point):
        flag = False


if flag == True:
    print("Yes")

else:
    print("No")
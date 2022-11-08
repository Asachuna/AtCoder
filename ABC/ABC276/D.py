N = int(input())
A = list(map(int, input().split()))

count = 0

def check(n):
    flagC = True
    for i in range(N):
        if A[i] %n != 0:
            flagC = False
            break
    
    return flagC

while check(2):
    for i in range(N):
        A[i] /= 2

while check(3):
    for i in range(N):
        A[i] /= 3


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

Afac = []
for i in range(N):
    Afac.append(prime_factorize(A[i]))


for i in range(N):
    fac = Afac[i]
    for ins in fac:
        if ins == 2:
            count += 1
            A[i] /= 2
        elif ins == 3:
            count += 1
            A[i] /= 3

corr = A[0]
flag = True

for a in A:
    if a != corr:
        flag = False
        break

if flag:
    print(count)
else:
    print(-1)
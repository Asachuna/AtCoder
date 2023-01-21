N, A, B = map(int, input().split())
S = list(input())
 
 
res = 10 ** 16
 
 
def get(i):
    if i < 0:
        return S[N+i]
 
    elif i < N:
        return S[i]
    else:
        return S[i-N]
 
if len(S)%2 != 0:
 
    for i in range(N):
        money = i * A
        mid = N//2+1-i

        for t in range((N//2)+1):

            if get(mid-t) != get(mid+t):
                money += B

                if money > res:
                    break
    
        res = min(res, money)
 
else:
    for i in range(N):
        money = i * A

        mid = N//2-i
        count = 0

        for t in range((N//2)):
            count += 1

            if get(mid-t) != get(mid+t+1):
                money += B

                if money > res:
                    break
        
        res = min(res, money)
    
 
print(res)
N = int(input())
 
count = 0
 
memo = {}

for a in range(1, N+1):
    for b in range(1, N//a+1):

        ab = a*b
        cd = N-ab

        res = 0
        
        if ab in memo:
            res = memo[ab]
        else:
            for c in range(1, int((cd)**0.5)+1):
                if (cd)%c == 0:
                    if cd == c**2:
                        res += 1
                    else:
                        res += 2
            
            memo[ab] = res
        
        count += res

 
print(count)
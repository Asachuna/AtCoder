N, M = map(int, input().split())

S = [list(input()) for _ in range(N)]

count = 0

for p in range(N):
    m1 = S[p]
    
    for p2 in range(N):
        if p < p2:

            m2 = S[p2]

            flag = True
            for i in range(M):
                if m1[i] != "o" and m2[i] != "o":
                    flag = False
                    break
            
            if flag:
                count += 1
    
print(count)
N = int(input())
H = list(map(int, input().split()))

max = -1
ans = -1
for i in range(N):
    if max <= H[i]:
        max = H[i]
        ans = i
    
print(ans+1)
N, W = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

#item, value -> weight
dp = [[10**16]*(10**5) for _ in range(N)]
fi = items[0]
dp[0][fi[1]] = fi[0]


for i in range(1, N):
    item = items[i]
    itemWeight = item[0]
    itemValue = item[1]
    for v in range(10**5):
        if v >= itemValue and dp[i-1][v-itemValue]+itemWeight <= W:
            dp[i][v] = min(dp[i-1][v], dp[i-1][v-itemValue]+itemWeight)
        else:
            dp[i][v] = dp[i-1][v]



res = 0
dplast = dp[N-1]
for i in range(10**5):
    if dplast[i] != 10**16:
        res = i

print(res)
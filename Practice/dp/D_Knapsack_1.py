N, W = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for _ in range(N)]
fi = items[0]
dp[0][fi[0]] = fi[1]

for i in range(1, N):
    for w in range(W+1):
        item = items[i]
        itemWeight = item[0]
        itemValue = item[1]

        if w >= itemWeight:
            dp[i][w] = max(dp[i-1][w-itemWeight] + itemValue, dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]


print(max(dp[N-1]))
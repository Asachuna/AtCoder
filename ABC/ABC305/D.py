import math

N = int(input())
dishes = []

for _ in range(N):
    x, y = map(int, input().split())
    dishes.append([x, y])

#お腹を壊している場合、壊していない場合それぞれのn皿目の最大値
dp = [[-math.inf, -math.inf] for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = 0

for i in range(N):
    dish = dishes[i]
    x = dish[0]
    y = dish[1]

    #解毒の場合
    if x == 0:
        dp[i+1][0] = max(dp[i][0], dp[i][0] + y, dp[i][1] + y)
        dp[i+1][1] = dp[i][1]

    #毒の場合
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][1], dp[i][0] + y)

print(max(dp[N][0], dp[N][1]))
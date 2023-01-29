N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [0] * (N+1)

dp[0] = 0
dp[1] = abs(H[0]-H[1])

for i in range(2, N):
    min_cost = 10 ** 16

    for j in range(min(K, i)):
        jump = j+1
        min_cost = min(dp[i-jump] + abs(H[i] - H[i-jump]), min_cost)

    dp[i] = min_cost

print(dp[N-1])
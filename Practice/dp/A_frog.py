#https://atcoder.jp/contests/dp/tasks

N = int(input())
H = list(map(int, input().split()))

dp = [10 ** 16] * (N+1)

dp[0] = 0
dp[1] = abs(H[0]-H[1])

for i in range(2, N):
    dp[i] = min(abs(H[i]-H[i-1]) + dp[i-1], abs(H[i]-H[i-2]) + dp[i-2])

print(dp[N-1])
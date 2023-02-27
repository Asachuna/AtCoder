N = int(input())

cards = []

for i in range(N):
    A, B = map(int, input().split())
    cards.append([A, B])

dp = [[0, 0] for _ in range(N)]

dp[0] = [1, 1]

for i in range(1, N):
    prevA = cards[i-1][0]
    prevB = cards[i-1][1]

    nextA = cards[i][0]
    nextB = cards[i][1]
    
    if nextA != prevA:
        dp[i][0] += dp[i-1][0]
    if nextA != prevB:
        dp[i][0] += dp[i-1][1]
    
    if nextB != prevA:
        dp[i][1] += dp[i-1][0]
    if nextB != prevB:
        dp[i][1] += dp[i-1][1]
    
    

print(sum(dp[N-1]) % 998244353)

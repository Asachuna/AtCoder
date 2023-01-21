n, x = map(int, input().split())
 
coins = []
 
for _ in range(n):
    A, B = map(int, input().split())
    coins.append([A, B])
 
# n * x の２次元配列を作成
dp = [[0]*(x + 1) for _ in range(n)]
 
# 1番目のコイン
for i in range(coins[0][1]+1):
    if i*coins[0][0] <= x:
        dp[0][i*coins[0][0]] = 1
 
# 2番目以降のコイン
for i in range(1,n):
    for j in range(x + 1):
        coin = coins[i]
        coinValue = coin[0]
        coinAmount = coin[1]
 
        ref = dp[i - 1][j]  # ref = reference(参照)の意味
 
        flag = 0

        if ref:
            flag = ref
        else:
            for amount in range(coinAmount+1):
                A = coinValue * amount
    
                if A > j:
                    if ref:
                        flag = 1
                    break
    
                else:
                    ref_back = dp[i - 1][j - A]
                    if ref or ref_back:
                        flag = 1
                        break
        
        dp[i][j] = flag
 
print("Yes" if dp[n-1][x] else "No")
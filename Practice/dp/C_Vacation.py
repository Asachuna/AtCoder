N = int(input())

acts = [list(map(int, input().split())) for _ in range(N)]

#日数, 前の日のアクティビティ
dp = [[0]*3 for _ in range(N+1)]

dp[0] = acts[0]

for i in range(1, N):
    act = acts[i]

    for index in range(3):
        ap = act[index]
        ot1, ot2 = 0, 0

        if index == 0:
            ot1 = 1
            ot2 = 2
        elif index == 1:
            ot1 = 0
            ot2 = 2
        elif index == 2:
            ot1 = 0
            ot2 = 1

        dp[i][index] = ap + max(dp[i-1][ot1], dp[i-1][ot2])

print(max(dp[N-1]))

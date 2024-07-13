from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
else:
    # 結果を格納する配列（インデックスは長さ-1に対応）
    result = [0] * N

    positions = defaultdict(list)
    for i, a in enumerate(A):
        positions[a].append(i)

    # 長さ1と2の等差数列をカウント
    result[0] = N
    result[1] = N * (N - 1) // 2
    for i in range(N):
        for j in range(i + 1, N):
            diff = A[j] - A[i]
            next_num = A[j] + diff
            if next_num in positions:
                for k in positions[next_num]:
                    if k > j:
                        length = 3
                        prev_j, prev_k = i, j
                        while True:
                            result[length - 1] += 1
                            next_num = A[k] + diff
                            if next_num not in positions:
                                break
                            next_positions = [pos for pos in positions[next_num] if pos > k]
                            if not next_positions:
                                break
                            prev_j, prev_k, k = prev_k, k, next_positions[0]
                            length += 1

    print(*result)
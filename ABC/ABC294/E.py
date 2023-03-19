L, n1, n2 = map(int, input().split())

compressed_row1 = []
for i in range(n1):
    v, l = map(int, input().split())
    compressed_row1.append((v, l))

compressed_row2 = []
for i in range(n2):
    v, l = map(int, input().split())
    compressed_row2.append((v, l))

i = 0
j = 0
cnt = 0

while i < n1 and j < n2:
    v1, l1 = compressed_row1[i]
    v2, l2 = compressed_row2[j]

    # v1 == v2の場合、同じ列に存在する
    if v1 == v2:
        cnt += min(l1, l2)
        i += 1
        j += 1
    # v1 < v2の場合、v1を含む列はv2を含む列よりも左にある
    elif v1 < v2:
        i += 1
    # v1 > v2の場合、v2を含む列はv1を含む列よりも左にある
    else:
        j += 1

print(cnt)
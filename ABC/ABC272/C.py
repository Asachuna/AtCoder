N = int(input())

A = list(map(int, input().split()))

even = []
odd = []

for i in A:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()

if len(even) < 2 and len(odd) < 2:
    print(-1)

else:
    oddmax, evenmax = -1, -1

    if len(odd) >= 2:
        oddmax = odd[len(odd)-1] + odd[len(odd)-2]

    if len(even) >= 2:
        evenmax = even[len(even)-1] + even[len(even)-2]
    
    print(max(oddmax, evenmax))
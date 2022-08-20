import itertools

N = int(input())
A = list(map(int, input().split()))

A.sort()
A.reverse()
As = [A[0], A[1], A[2]]

As = itertools.permutations(As)

nums = []

for a in As:
    a = list(a)
    i = ""
    for l in a:
        i += str(l)
    
    i = int(i)
    nums.append(i)

print(max(nums))

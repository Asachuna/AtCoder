N = int(input())
A = list(map(int, input().split()))

answers = {}

for a in A:
    if (a not in answers):
        answers[a] = 1

keys = sorted(list(answers.keys()))

prevKey = None

for key in keys:
    if prevKey:
        answers[key] += answers[prevKey]
    
    prevKey = key
    

length = len(answers.keys())

ks = {}

for a in A:
    res = length - answers[a]
    if res in ks:
        ks[res] += 1
    else:
        ks[res] = 1

for k in range(N):
    if k in ks:
        print(ks[k])
    else:
        print(0)

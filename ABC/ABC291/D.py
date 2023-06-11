N = int(input())

cards = []

for i in range(N):
    A, B = map(int, input().split())
    cards.append([A, B])

patA = 1
patB = 1

for i in range(1, N):
    prevA = cards[i-1][0]
    prevB = cards[i-1][1]

    nextA = cards[i][0]
    nextB = cards[i][1]

    nextPatA = 0
    nextPatB = 0

    if prevA != nextA:
        nextPatA += patA
    
    if prevB != nextA:
        nextPatA += patB

    if prevA != nextB:
        nextPatB += patA

    if prevB != nextB:
        nextPatB += patB
        
        
    
    patA, patB = nextPatA, nextPatB

print((patA+patB) % 998244353)
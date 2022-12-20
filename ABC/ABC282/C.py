N = int(input())

S = list(input())

surround = False

for i in range(N):
    if not surround:
        if S[i] == '"':
            surround = True
        elif S[i] == ',':
            S[i] = '.'
    
    else:
        if S[i] == '"':
            surround = False

print("".join(S))
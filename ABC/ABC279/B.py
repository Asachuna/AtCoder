S = input()
T = input()

ans = "No"

for i in range(len(S)):
    if S[i] == T[0]:
        flag = True
        for x in range(len(T)):
            if i+x >= len(S):
                flag = False
                break
            else:
                if S[i+x] != T[x]:
                    flag = False
                    break
        
        if flag:
            ans = "Yes"
            break


print(ans)
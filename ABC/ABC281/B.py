S = list(input())

nums = list("0123456789")

flag = True

if len(S) != 8:
    flag = False

else:
    if S[0] in nums or S[7] in nums:
        flag = False
    
    else:
        if S[1] == "0":
            flag = False
        else:
            for i in range(6):
                if S[i+1] not in nums:
                    flag = False

if flag:
    print("Yes")
else:
    print("No")
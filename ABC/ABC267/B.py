c1 = [7]
c2 = [4]
c3 = [8, 2]
c4 = [1, 5]
c5 = [3, 9]
c6 = [6]
c7 = [10]

cs = [c1, c2, c3, c4, c5, c6, c7]

S = list(input())

def checkCol(c):
    for i in c:
        if int(S[i-1]) == 1:
            return False
    return True


if int(S[0]) == 1:
    print("No")

else:
    flag = False
    allDown = []
    for c in cs:
        allDown.append(checkCol(c))
    
    for i in range(7):
        if allDown[i] == False:
            l = False
            for j in range(7-i-1):
                if(allDown[i+j+1]) == True:
                    l = True
                elif l == True:
                    flag = True
                    break
    
    if flag:
        print("Yes")
    else:
        print("No")
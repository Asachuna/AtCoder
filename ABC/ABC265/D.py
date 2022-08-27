N, p, q, r = map(int, input().split())
A = list(map(int, input().split()))



numSum = p+q+r

def getSum(left, right):
    return sum(A[left:right])

def hantei(left, right):
    aPart = A[left:right]
    sumPart = 0
    arr = [p, q, r]
    index = 0

    for a in aPart:
        sumPart += a
        if arr[index] == sumPart:
            index += 1
            sumPart = 0
    
    return index==3


right = 0
partSum = -1
flag = False

for left in range(N):
    partSum = getSum(left, right)

    while not flag and right < N and partSum <= numSum:
        partSum = getSum(left, right)

        if partSum == numSum:
            if (hantei(left, right)):
                flag = True

        right += 1

    right -= 1

    if left == right:
        right += 1    

    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")

x, y, n = map(int, input().split())

if y/3 > x:
    print(x*n)
else:
    price = 0
    count = 0
    loop = True
    while loop:
        if n-count >= 3:
            count += 3
            price += y
        else:
            count += 1
            price += x
        

        if count >= n:
            loop = False
            print(price)
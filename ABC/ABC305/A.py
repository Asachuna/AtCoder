N = int(input())

road = N%5
if (road <= 2):
    print(N-N%5)
else:
    print(N+(5-N%5))
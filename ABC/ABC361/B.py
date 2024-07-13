a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

def check(a1, a2, b1, b2):
  return (a2 > b1 and a1 < b2) or (a2 < b1 and a1 > b2)

yes = check(a, d, g, j) and check(b, e, h, k) and check(c, f, i, l)

if yes:
  print("Yes")

else:
  print("No")
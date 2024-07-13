x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

d1 = (x1-x2) ** 2 + (y1-y2) ** 2
d2 = (x2-x3) ** 2 + (y2-y3) ** 2
d3 = (x3-x1) ** 2 + (y3-y1) ** 2

flag = False
if max(d1, d2, d3) == d1:
  if d1 == d2 + d3:
    flag = True
if max(d1, d2, d3) == d2:
  if d2 == d1 + d3:
    flag = True
if max(d1, d2, d3) == d3:
  if d3 == d2 + d1:
    flag = True

if flag:
  print("Yes")
else:
  print("No")
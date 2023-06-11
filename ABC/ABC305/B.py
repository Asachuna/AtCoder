points = [0, 3, 4, 8, 9, 14, 23]
a = "ABCDEFG"
p, q = input().split()

pi, qi = a.index(p), a.index(q)
if qi > pi:
    pi, qi = qi, pi

print(points[pi] - points[qi])
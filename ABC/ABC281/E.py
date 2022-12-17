v = [2]
l = [[1], [3], [5], [7], [9]]


def swap(a, b):
    temp = a[0]
    a[0] = b[0]
    b[0] = temp

swap(v, l[0]);
swap(l[0], l[1]);
swap(v, l[0]);

print(v, l)
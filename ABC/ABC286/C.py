from collections import defaultdict
import sys
sys.setrecursionlimit(100000000000)


class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        #各要素の親要素の番号を格納するリスト
        #要素がrootの場合は -(配下要素数) を格納する
        self.parents = [-1] * n
    
    #木を統合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        #すでに同じ木に属する場合
        if x == y:
            return
        
        #xよりyの方が要素数が多い場合、xとyを入れ替え
        #これにより、 size(y) <= size(x)が保証される
        if self.parents[x] < self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #親を取得
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N, M = map(int, input().split())

uf = UnionFind(N)

path = [list(map(int, input().split())) for _ in range(M)]

connect = [0] * N
flag = True

for p in path:
    p1 = p[0] - 1
    p2 = p[1] - 1

    if connect[p1] < 2 and connect[p2] < 2:
        uf.union(p1, p2)
        connect[p1] += 1
        connect[p2] += 1
    else:
        flag = False
        break

if uf.group_count() != 1:
    flag = False

two = 0
one = 0

for c in connect:
    if c == 2:
        two += 1
    if c == 1:
        one += 1

if flag and two == N-2 and one == 2:
    print("Yes")
else:
    print("No")
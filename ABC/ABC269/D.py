N = int(input())

tonari = [[-1, -1], [-1, 0], [0, -1], [0, 1] , [1, 0], [1, 1]]

from collections import defaultdict

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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

uf = UnionFind(N)

points = []

for p in range(N):
    X, Y = map(int, input().split())
    for t in tonari:
        for pindex in range(len(points)):
            if X + t[0] == points[pindex][0]  and Y + t[1] == points[pindex][1]:
                uf.union(p, pindex)
                break
    
    points.append([X, Y])

print(len(uf.roots()))
        

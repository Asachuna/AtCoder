H, W = map(int, input().split())

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

allmap = []

for _ in range(H):
    allmap.append(list(input()))

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

uf = UnionFind(H*W)

start = []

for y in range(H):
    for x in range(W):
        if allmap[y][x] == "S":
            start = [x, y]
            break

startX = start[0]
startY = start[1]

def colToID(x, y):
    return y*W + x

queue = []


def pushQueue(x, y):
    newq = [[[[x+dir[0], y+dir[1]] for dir in directions], [x, y]]]
    for q in newq:
        queue.append(q)

pushQueue(startX, startY)

print(queue)

while len(queue) != 0:
    curQ = queue[0]
    lastX = curQ[1][0]
    lastY = curQ[1][1]

    x = curQ[0][0]
    y = curQ[0][1]

    if x >= 0 and x < W and y >= 0 and y < H:
        if allmap[y][x] == ".":
            pushQueue(x, y)
            uf.union(colToID(x, y), colToID(lastX, lastY))

    queue.pop(0)






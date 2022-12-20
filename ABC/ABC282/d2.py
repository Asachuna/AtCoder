import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict 

N,M = map(int,input().split())

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


uf = UnionFind(N)
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))  
    a,b = a-1, b-1

    dict[a].add(b)
    dict[b].add(a)
    uf.union(a, b)

color = [0 for i in range(N+1)]

def dfs(v,c,queue=[]):
    u'''
    v : 現在のグラフの頂点
    c : 現在参照するフラグ,1=>-1=>1と使うので渡す必要がある
    queue : 探索したグラフの頂点を入れていく
    res : global変数を使いたくないが,再帰のreturnがよくわからないのでとりあえず
    '''

    global color
    global res 
    queue.append(v)

    for i in list(dict[v]):
        if color[i] == c:#隣の頂点が同じ値を与えられている際Falseを返す
            res = False
        elif i not in queue:#探索済みでなければ再帰する
            color[i] = c*-1#0ならcとは異なる値を格納
            dfs(i,-c,queue)#引数に-cとすることで,cが1=>-1=>1を繰り返す

results = {}
roots = uf.roots()

#雑
res = True

activePoints = 0

for i in range(len(roots)):
    res = True
    root = roots[i]
    color[root] = 1
    dfs(root, 1)
    results[root] = res
    
    if res:
        activePoints += uf.size(root)
r = 0


for i in range(len(roots)):
    root = roots[i]
    members = uf.members(root)


    if results[root] == True:
        selfCount = 0


        #他グループとの結合
        otherCount = activePoints - len(members)


        #自グループとの結合
        c1 = 0
        c2 = 0
        lines = 0

        for m in members:
            if color[m] == -1:
                c1 += 1
            else:
                c2 += 1
            
            lines += len(dict[m])

        selfCount = c1 * c2 - lines//2
    
        r += selfCount + otherCount

print(r)

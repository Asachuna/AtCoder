N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ASum = sum(A)

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
        #if self.parents[x] < self.parents[y]:
        #    x, y = y, x
        
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

current_num = A[0]
#現在区間の始点
parent = 0

end = {}

for i in range(N):
    if A[i] == current_num or A[i] == current_num+1:
        uf.union(parent, i)
    else:
        end[parent] = i-1
        parent = i
    
    current_num = A[i]

end[parent] = N-1

print([uf.find(i) for i in range(N)])


if A[0] == 0 and A[N-1] == M-1:
    uf.union(N-1, 0)
    end[parent] += end[0]+1

tableSum = []


print(uf.roots())
print(end)

for root in uf.roots():
    print([(root+i)%M for i in range(end[root]-root)])
    members = [A[(root+i)%M] for i in range(end[root]-root)]
    print(members)
    tableSum.append(sum(members))



print(ASum - max(tableSum))

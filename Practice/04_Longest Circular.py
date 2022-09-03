N = int(input())

class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = [-1] * N

    def find(self, x, c=0):
        if self.parents[x] < 0:
            return (x, c)
        else:
            return self.find(self.parents[x], c+1)
    
    def union(self, x, y):
        self.parents[x] = y

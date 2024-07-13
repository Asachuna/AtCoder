import sys
sys.setrecursionlimit(10000000)

N = int(input())
roads = []

for i in range(N-1):
  A, B, C = map(int,input().split())
  roads.append([A, B, C])

map = {}

for i in range(N):
  map[i+1] = []

roadSum = 0

for road in roads:
  a, b, c = road
  roadSum += c
  map[a].append([b, c])
  map[b].append([a, c])

def dfs(node, parent, depth):
    max_depth = depth
    farthest_node = node
    for child, length in map[node]:
        if child != parent:
            child_depth, child_farthest = dfs(child, node, depth + length)
            if child_depth > max_depth:
                max_depth = child_depth
                farthest_node = child_farthest
    return max_depth, farthest_node

def find_tree_diameter():
    _, farthest = dfs(1, -1, 0)
    diameter, _ = dfs(farthest, -1, 0)
    return diameter


diameter = find_tree_diameter()
print(roadSum * 2 - diameter)
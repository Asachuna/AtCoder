import heapq

def dijkstra_with_vertex_weights(graph, vertex_weights, start, N):
    distances = [float('infinity')] * N
    distances[start] = vertex_weights[start]
    pq = [(vertex_weights[start], start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, edge_weight in graph[current_vertex]:
            distance = current_distance + edge_weight + vertex_weights[neighbor]
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int, input().split())
    U -= 1
    V -= 1
    graph[U].append((V, B))
    graph[V].append((U, B))

start_vertex = 0
result = dijkstra_with_vertex_weights(graph, A, start_vertex, N)

result.pop(0)
print(*result)
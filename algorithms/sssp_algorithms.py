import math
from collections import defaultdict
from heapq import *

def dijkstra(graph, n, s, path):

    dist = [math.inf for _ in range(n)]
    visited = [False for _ in range(n)]

    path[s] = -1
    dist[s] = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if not visited[j] and (v == -1 or dist[j] < dist[v]):
                v = j
        
        if dist[v] == math.inf:
            break
        
        visited[v] = True
        for neigh in graph[v]:
            node, length = neigh
            if dist[v] + length < dist[node]:
                dist[node] = dist[v] + length
                path[node] = v

def dijkstra_opt(graph, n, s):

    dist = [math.inf for _ in range(n)]

    dist[s] = 0
    heap = [(0, s)]

    while heap:
        d_v, v = heappop(heap)

        if dist[v] != d_v:
            continue

        for neigh in graph[v]:
            node, length = neigh
            if dist[v] + length < dist[node]:
                dist[node] = dist[v] + length
                heappush(heap, (dist[node], node))
    
    return dist

def bellman_ford(edges, n, a, s):
    dist = [-math.inf] * (n)
    dist[s] = 0

    for k in range(a):
        temp = [-math.inf] * n
        for a, b, c in edges:
            temp[b] = max(temp[b], dist[b], dist[a] + c)
        # print(temp)
        dist = temp
    return dist

n = int(input())
q = int(input())

graph = defaultdict(list)
for _ in range(q):
    a, b, c = [int(v) for v in input().split()]
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

path = [-1 for _ in range(n)]
print(graph)
dijkstra(graph, n, 0, path)
print(path)


    

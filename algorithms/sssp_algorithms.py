import math
from collections import defaultdict
from heapq import *

def dijkstra(graph, n, s):
    dist = [math.inf for _ in range(n)]
    visited = [False for _ in range(n)]
    dist[s] = 0
    for i in range(n):
        v = -1
        for j in range(n): # First find shortest distance
            if not visited[j] and (v == -1 or dist[j] < dist[v]):
                v = j
        if dist[v] == math.inf: # in case no node is reachable
            break
        visited[v] = True
        for neigh in graph[v]: # Then do the relaxation work 
            node, length = neigh
            if dist[v] + length < dist[node]:
                dist[node] = dist[v] + length

def dijkstra_opt(graph, source):
    """
    Finds the shortest path from `source` to each other node.
    
    Assumes that the graph is given as an adjacency list (list of list), each node should be indexed
    from 0 to V - 1, where V is the number of vertex in the graph.
    The algorithm works ONLY when all edges have positive weights.

    Time complexity : O(E log(V))
    """
    n = len(graph)
    dist = [math.inf for _ in range(n)]

    dist[source] = 0
    heap = [(0, source)]

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

def bellman_ford(edges, n, s, iterations=None):
    """
    edges: list of (u, v, w) tuples, a directed edge u -> v with weight w
    n: number of nodes
    s: source node
    iterations: number of relaxation rounds (default n - 1, enough for any shortest path)

    Assumes the nodes in the graph are labeled from 0 to n - 1.
    Time complexity : O(V * E)
    returns (has_negative_cycle, dist)
    """
    if iterations is None:
        iterations = n - 1

    dist = [math.inf for _ in range(n)]
    dist[s] = 0

    for _ in range(iterations):
        updated = False

        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True

        if not updated:  # early stop: distances are stable
            break

    # If anything can still be relaxed, there is a negative cycle
    has_negative_cycle = any(dist[u] + w < dist[v] for u, v, w in edges)

    return has_negative_cycle, dist


    

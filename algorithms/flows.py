from collections import deque

def scaling(n, t_edges, s, t):
    """
    t_edges : list of all edges in the graph (from, to, capacity).
    n : number of nodes
    s : source
    t : sink

    Finds the maximum flow from s (source) to t (sink).
    Time complexity : O(E² log(C))
    C is an upper bound of the threshold capacity we can add
    at each augmenting path we can find, which is fixed at 2^62.

    returns : (max_flow, residual_graph)
    """

    edges = []

    graph = [[] for _ in range(n)]
    M = len(t_edges)
    for i in range(M):
        a, b, c = t_edges[i]
        graph[a].append(2 * i)
        graph[b].append(2 * i + 1)
        edges.append([a, b, c])
        edges.append([b, a, 0])
        
    def dfs(u, th):
        stack = [u]
        coming_from = [-2] * n
        coming_from[u] = -1

        while stack:
            node = stack.pop()

            for ind in graph[node]:
                vfrom, vto, vcap = edges[ind]
                if vcap >= th and coming_from[vto] == -2:
                    stack.append(vto)
                    coming_from[vto] = ind

        if coming_from[t] == -2:
            return False

        where = coming_from[t]
        while where != -1:
            edges[where][2] -= th # normal
            edges[where ^ 1][2] += th # reverse
            vfrom = edges[where][0]
            where = coming_from[vfrom]

        return True

    threshold = (1 << 62)
    max_flow = 0
    while threshold > 0:

        while dfs(s, threshold):
            max_flow += threshold
        threshold >>= 1

    residual = [[] for _ in range(n)]
    for ufrom, uto, ucap in edges:
        residual[ufrom].append((uto, ucap))

    return max_flow, residual

def edmond_karp(graph, n, m):
    """
    (not useful, use scaling algorithm, it's more efficient)
    The idea is, as long as there is an increasing path (meaning that we can go from
    the source to the sink and find a total_flow > 0), we use this path increase 
    capacities.
    Time complexity : O(N * M²)
    """
    max_so_far = 0
    while True:
        queue = deque([(-1, 1, 10**18)])
        visited = [0] * (n + 1)
        visited[1] = 1
        parent = [-2] * (n + 1)

        total_flow = 0

        while queue:
            prev, node, flow = queue.pop()
            parent[node] = prev

            if node == n:
                total_flow = flow
                break

            for i in graph[node]:
                neigh, capacity = i, graph[node][i]
                if capacity and not visited[neigh]:
                    visited[neigh] = 1
                    queue.appendleft((node, neigh, min(flow, capacity)))
            #print(stack)
        if total_flow != 0:
            curr = n
            max_so_far += total_flow
            while curr != -1:
                if parent[curr] != -1:
                    graph[curr][parent[curr]] += total_flow
                    graph[parent[curr]][curr] -= total_flow
                curr = parent[curr]
        else:
            break

    return max_so_far
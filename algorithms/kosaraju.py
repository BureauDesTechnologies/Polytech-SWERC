def kosaraju(edges, n):
    """
    Finds the SCC of the directed graph.
    Time complexity : O(n)
    """
 
    graph = [[] for _ in range(n)]
    rgraph = [[] for _ in range(n)]
 
    for a, b in edges:
        graph[a].append(b)
        rgraph[b].append(a)
 
    visited = [False] * n
    order = []
 
    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        stack = [(start, 0)]
        while stack:
            node, idx = stack.pop()
            if idx < len(graph[node]):
                stack.append((node, idx + 1))
                nxt = graph[node][idx]
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
 
    comp = [-1] * n
    c = 0
    for start in reversed(order):
        if comp[start] != -1:
            continue
        comp[start] = c
        stack = [start]
        while stack:
            node = stack.pop()
            for nxt in rgraph[node]:
                if comp[nxt] == -1:
                    comp[nxt] = c
                    stack.append(nxt)
        c += 1
 
    return comp
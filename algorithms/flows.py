
def ford_fulkerson(graph, n, m):
    max_so_far = 0
    while True:
        stack = [(-1, 1, 10**18)]
        parent = [-2] * (n + 1)

        total_flow = 0

        while stack:
            prev, node, flow = stack.pop()
            parent[node] = prev

            if node == n:
                total_flow = flow
                break

            for i in graph[node]:
                neigh, capacity = i, graph[node][i]
                if capacity and parent[neigh] == -2:
                    stack.append((node, neigh, min(flow, capacity)))
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
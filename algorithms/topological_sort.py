"""
Topological sort on a DAG provides a linear view of the graph (in a list)
such that, when iterating in the list, for each edge u -> v, u is visited before v.
"""

# DFS version - Classic version
import sys

MAX_N = 10**5
sys.setrecursionlimit(MAX_N)


def dfs(node: int) -> None:
	for next_ in graph[node]:
		if not visited[next_]:
			visited[next_] = True
			dfs(next_)
	top_sort.append(node)


# The number of nodes and edges respectively
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n)]

for _ in range(m):
	a, b = map(int, input().strip().split())
	graph[a - 1].append(b - 1)

visited = [False] * n
top_sort = []
for i in range(n):
	if not visited[i]:
		visited[i] = True
		dfs(i)
top_sort = top_sort[::-1]

ind = [0] * n
for i in range(n):
	ind[top_sort[i]] = i

# Check if the topological sort is valid
# valid = True
# for i in range(n):
# 	for j in graph[i]:
# 		if ind[j] <= ind[i]:
# 			valid = False
# 			break

# 	if not valid:
# 		break

# if valid:
# 	print(*[i + 1 for i in top_sort])
# else:
# 	print("IMPOSSIBLE")

# BFS version - Kahn's algorithm
"""
Allows to find the lexicographically minimum / maximum topological sort.
Use heap for this effect ... 
"""
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a - 1].append(b - 1)

in_degree = [0 for _ in range(n)]
for nodes in graph:
	for node in nodes:
		in_degree[node] += 1

queue = deque([i for i, in_deg in enumerate(in_degree) if in_deg == 0])
top_sort = []
while queue:
	curr = queue.popleft()
	top_sort.append(curr)
	for next_ in graph[curr]:
		in_degree[next_] -= 1
		if in_degree[next_] == 0:
			queue.append(next_)

if len(top_sort) == n:
	print(*[x + 1 for x in top_sort])
else:
	print("IMPOSSIBLE")

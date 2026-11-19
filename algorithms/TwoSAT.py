from collections import defaultdict
 
class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]
        self.rgraph = [[] for _ in range(2 * n)]
        self.comp = [-1] * (2 * n)
        self.nb_scc = 0
        self.solved = False
        self.satisfiable = None
        self.assignment = None
 
    def _node(self, var, value):
        return 2 * var + (0 if value else 1)
 
    def add_clause(self, a, va, b, vb):
        """
        Add clause "(va a or vb b)" where va and vb are respectively the sign of a and b.
        Beware that 0 <= a, b < n. (n is the number of nodes in the graph, each node is indexed from 0 to n - 1)
        Time complexity : O(1) 
        """
        na = self._node(a, va)
        nb = self._node(b, vb)
        self.graph[na ^ 1].append(nb)
        self.graph[nb ^ 1].append(na)
        self.rgraph[nb].append(na ^ 1)
        self.rgraph[na].append(nb ^ 1)
        self.solved = False
 
    def _kosaraju(self):
        """
        Finds the SCC of the directed graph.
        Time complexity : O(n)
        """
        size = 2 * self.n
        visited = [False] * size
        order = []
 
        for start in range(size):
            if visited[start]:
                continue
            visited[start] = True
            stack = [(start, 0)]
            while stack:
                node, idx = stack.pop()
                if idx < len(self.graph[node]):
                    stack.append((node, idx + 1))
                    nxt = self.graph[node][idx]
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(node)
 
        self.comp = [-1] * size
        c = 0
        for start in reversed(order):
            if self.comp[start] != -1:
                continue
            self.comp[start] = c
            stack = [start]
            while stack:
                node = stack.pop()
                for nxt in self.rgraph[node]:
                    if self.comp[nxt] == -1:
                        self.comp[nxt] = c
                        stack.append(nxt)
            c += 1
        self.nb_scc = c
 
    def solve(self):
        """
        Find if the 2-CNF is satisfiable.
        Time complexity : O(n)
        """
        self._kosaraju()
        self.satisfiable = True
        self.assignment = [False] * self.n
        for i in range(self.n):
            if self.comp[2 * i] == self.comp[2 * i + 1]:
                self.satisfiable = False
                self.assignment = None
                break
            self.assignment[i] = self.comp[2 * i] > self.comp[2 * i + 1]
        self.solved = True
        return self.satisfiable
 
    def is_satisfiable(self):
        if not self.solved:
            self.solve()
        return self.satisfiable
 
    def get_assignment(self):
        if not self.solved:
            self.solve()
        return self.assignment
 
    def get_scc_count(self):
        if not self.solved:
            self.solve()
        return self.nb_scc
class DSU:

    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n
        self.size = n
    
    def find(self, e):
        """
        Find the representant of e.
        Time complexity : O(a(n)) where a is the inverse ackermann function (grows very very slow)
        """
        if not (0 <= e < self.size):
            return None
    
        comp = [e]
        curr = e
        while self.parents[comp[-1]] != comp[-1]:
            comp.append(self.parents[curr])
            curr = self.parents[curr]
    
        u = comp.pop()
        while comp:
            self.parents[comp.pop()] = u 
        
        return self.parents[e]
    
    def union(self, e1, e2):
        """
        Groups together the set of e1 and e2.
        Time complexity : O(a(n)) where a is the inverse ackermann function (grows very very slow)
        """

        r1, r2 = self.find(e1), self.find(e2)
        if r1 == r2:
            return
        
        if self.rank[r1] < self.rank[r2]:
            r1, r2 = r2, r1
        
        self.parents[r2] = r1

        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1
    
    def is_same_set(self, e1, e2):
        return self.find(e1) == self.find(e2)
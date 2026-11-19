class LazySegTree:
 
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
 
        self.array = [0] * (2 * self.size)
        self.array2 = [0] * (2 * self.size)
 
    def build(self, array):
        """
        O(n)
        """
 
        for i in range(len(array)):
            self.array[self.size - 1 + i] = array[i]

        for j in range(self.size - 2, -1, -1):
            self.array[j] = self.array[2 * j + 1] + self.array[2 * j + 2]
 
    def range_update(self, sx, sy, v):
        """
        O(log n)
        """
        if sx == sy:
            return

        stack = [(0, 0, self.size, False)]

        while stack:
            nx, nlx, nly, processed = stack.pop()

            if processed:
                self.array[nx] = self.array[2 * nx + 1] + self.array[2 * nx + 2]
                continue

            if nly <= sx or nlx >= sy: # outside
                continue

            if self.array2[nx] != 0 and nx < self.size - 1:
                self.array2[2 * nx + 1] += self.array2[nx]
                self.array[2 * nx + 1] += (nly - nlx) // 2 * self.array2[nx]
                self.array2[2 * nx + 2] += self.array2[nx]
                self.array[2 * nx + 2] += (nly - nlx) // 2 * self.array2[nx]
                self.array2[nx] = 0

            # Completely inside
            if sx <= nlx and nly <= sy:
                self.array2[nx] += v
                self.array[nx] += (nly - nlx) * v
                continue

            stack.append((nx, nlx, nly, True))

            m = (nlx + nly) // 2
            stack.append((2 * nx + 2, m, nly, False))
            stack.append((2 * nx + 1, nlx, m, False))

    def point_update(self, i, v):
        self.range_update(i, i + 1, v)
    
    def range_query(self, sx, sy):
        stack = [(0, 0, self.size, 0)]
        
        if sx == sy:
            return
 
        current = 0
 
        while stack:
            nx, nlx, nly, v1 = stack.pop()
 
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                current += self.array[nx] + (nly - nlx) * v1
                continue

            v1 += self.array2[nx]
 
            m = (nlx + nly) // 2
 
            if sy < m:
                stack.append((2 * nx + 1, nlx, m, v1))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly, v1))
            else:
                stack.append((2 * nx + 2, m, nly, v1))
                stack.append((2 * nx + 1, nlx, m, v1))
 
        return current

    def point_query(self, i):
        return self.range_query(i, i + 1)


"""
Version with only one operation.
"""

class SegTree:
 
    def __init__(self, n, callback):
        self.size = 1
        while self.size < n:
            self.size *= 2
 
        self.callback = callback
        self.array = [0] * (2 * self.size)
 
    def update(self, sx, sy, v):
        stack = [(0, 0, self.size)]
 
        if sx == sy:
            return
 
        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                self.array[nx] = self.callback(self.array[nx], v)
                continue
 
            m = (nlx + nly) // 2
 
            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 1, nlx, m))
                stack.append((2 * nx + 2, m, nly))
    
    def query(self, i):
        stack = [(0, 0, self.size)]
 
        current = 0
 
        while stack:
            nx, nlx, nly = stack.pop()
 
            current = self.callback(self.array[nx], current)
 
            if nly - nlx == 1:
                return current
            
            stack.append((nx, nlx, nly))
            m = (nlx + nly) // 2
 
            if i < m:
                stack.append((2 * nx + 1, nlx, m))
            else:
                stack.append((2 * nx + 2, m, nly))
 
        return current
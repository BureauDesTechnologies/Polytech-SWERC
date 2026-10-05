class LazySegTree:
 
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
 
        self.array = [10**18] * (2 * self.size)
        self.array2 = [0] * (2 * self.size)
 
    def build(self, array):
        """
        O(n)
        """
 
        for i in range(len(array)):
            self.array[self.size - 1 + i] = array[i]

        for j in range(self.size - 2, -1, -1):
            self.array[j] = min(self.array[2 * j + 1], self.array[2 * j + 2])
 
    def update(self, sx, sy, v):
        """
        O(log n)
        """
        if sx == sy:
            return

        stack = [(0, 0, self.size, False)]

        while stack:
            nx, nlx, nly, processed = stack.pop()

            if processed:
                self.array[nx] = min(self.array[2 * nx + 1], self.array[2 * nx + 2]) + self.array2[nx]
                continue

            if nly <= sx or nlx >= sy: # outside
                continue

            if self.array2[nx] != 0 and nx < self.size - 1:
                self.array2[2 * nx + 1] += self.array2[nx]
                self.array[2 * nx + 1] += self.array2[nx]
                self.array2[2 * nx + 2] += self.array2[nx]
                self.array[2 * nx + 2] += self.array2[nx]
                self.array2[nx] = 0

            # Completely inside
            if sx <= nlx and nly <= sy:
                self.array2[nx] += v
                self.array[nx] += v
                continue

            stack.append((nx, nlx, nly, True))

            m = (nlx + nly) // 2
            stack.append((2 * nx + 2, m, nly, False))
            stack.append((2 * nx + 1, nlx, m, False))
    
    def query(self, sx, sy):
        stack = [(0, 0, self.size, 0)]
        
        if sx == sy:
            return
 
        current = 10**18
 
        while stack:
            nx, nlx, nly, v1 = stack.pop()
 
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                current = min(current, self.array[nx] + v1)
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
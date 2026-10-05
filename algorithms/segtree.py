
"""
Version top -> bottom
"""
class SegTree:

    def __init__(self, n, callback, neutral):
        """
        Initialize the segment tree.
        All values are set to ``neutral``.
        We assume that ``callback`` is associative.
        """
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.callback = callback
        self.array = [neutral] * (2 * self.size)
        self.neutral = neutral

    def build(self, array):
        """
        Constructs the segment tree from array data in O(n).
        """

        for i in range(len(array)):
            self.array[self.size - 1 + i] = array[i]

        for i in range(self.size - 2, -1, -1):
            self.array[i] = self.callback(self.array[2 * i + 1], self.array[2 * i + 2])

    def query(self, sx, sy):
        """
        Returns range operation of [sx, sy) in O(log n).
        """
        stack = [(0, 0, self.size)]
        current_value = self.neutral

        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                current_value = self.callback(current_value, self.array[nx])
                continue

            m = (nlx + nly) // 2

            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 2, m, nly))
                stack.append((2 * nx + 1, nlx, m))
        
        return current_value
    
    def update(self, val, i):
        """
        Updates value at index i with ``val`` in O(log n).
        """
        stack = [(0, 0, self.size, False)]

        while stack:
            nx , nlx, nly, computable = stack.pop()

            if nly - nlx == 1:
                self.array[nx] = val
                continue
            
            if not computable:
                stack.append((nx, nlx, nly, True))
                m = (nlx + nly) // 2

                if i < m:
                    stack.append((2 * nx + 1, nlx, m, False))
                else:
                    stack.append((2 * nx + 2, m, nly, False))
            else:
                self.array[nx] = self.callback(self.array[2 * nx + 1], self.array[2 * nx + 2])

callback_min = min
callback_max = max
callback_sum = lambda u, v : u + v
callback_xor = lambda u, v : u ^ v


"""
Version bottom -> top
"""

SIZE = (1 << 20)

def build(l, tree):

    N = len(l)
    for i in range(N):
        tree[i + SIZE] = l[i]
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

def query(l, r, tree):

    res = 0
    l += SIZE
    r += SIZE

    while l <= r:
        if l & 1:
            res += tree[l]
            l += 1
        if r & 1 == 0:
            res += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    
    return res


def update(x, v, tree):

    x += SIZE
    tree[x] = v
    while x > 1:
        x >>= 1
        tree[x] = tree[2 * x] + tree[2 * x + 1]
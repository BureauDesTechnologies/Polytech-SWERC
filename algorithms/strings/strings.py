from collections import deque
class Vertex:
    """
    Vertex of the Aho-Corasick trie
    Credits: TryAlgo - Christoph Dürr
    """

    LOW = ord('a')  # Ascii code of smallest letter in the alphabet
    LEN = 26        # Alphabet size

    def index(ch):  # transforms the character into internal index
        i = ord(ch) - Vertex.LOW
        assert 0 <= i < Vertex.LEN
        return i

    def __init__(self):
        self.pattern = -1 # -1 means no pattern, otherwise it is the pattern index
        self.next   = [None] * Vertex.LEN
        self.suffix = None
        self.output = None    

class Aho_Corasick:

    def __init__(self, patterns):
        """patterns is a list of strings. 
        Later when we search for them, we return only their index in that list 
        and the matching position.
        
        :complexity: O(sum(map(len, patterns)))
        """
        # 1. build the trie
        self.root = Vertex()
        for pattern_index, p in enumerate(patterns):        
            # add pattern p to the trie
            v = self.root   # current vertex in the tree ...
            for ch in p:    # ... corresponding to a prefix of p
                i = Vertex.index(ch)
                if v.next[i] is None:   # create vertices on the fly
                    v.next[i] = Vertex()
                v = v.next[i]           # descend in the trie
            v.pattern = pattern_index   # mark that this is a pattern
        # 2. augment with suffix and output links
        # and turn it into a full automaton
        Q = deque()               # queue of vertices to be processed
        # start with the root
        for i, v in enumerate(self.root.next):     
            if v is None:
                self.root.next[i] = self.root
            else:
                v.suffix = self.root 
                Q.appendleft(v)             # initially Q contains the first level vertices
        while Q:
            u = Q.pop()                     # process u
            for i, v in enumerate(u.next):  # all arcs u -> v labeled i
                if v is None:
                    u.next[i] = u.suffix.next[i]
                else:
                    Q.appendleft(v)
                    v.suffix = u.suffix.next[i]
            if u.suffix.pattern != -1:
                u.output = u.suffix
            else:
                u.output = u.suffix.output 
                
    def match(self, s):
        """ find all substrings of s which are among the stored strings.
            Iterates over positions in s and the matched string ending at this position.
        """
        v = self.root               # current vertex
        for j, ch in enumerate(s):
            i = Vertex.index(ch)    # descend one step
            v = v.next[i] 
            a = v                   # now output all found patterns
            while a is not None:
                if a.pattern != -1: # this test can fail only for v itself
                    yield(j, a.pattern)
                a = a.output        # follow the output links

def poly_hash(s, M, p):
    """
    Generates prefix hashes of s, using modulo ``M`` and prime ``p``, in O(n).
    Returns ``ps`` (prefix hashes) and ``inv_pw`` (precomputed inverse power of each ``p**k``)
    """

    N = len(s)
    ps = [0] * (N + 1)
    
    pw1 = 1
    for i in range(N):
        v = ord(s[i]) - ord("a")
        ps[i] = (ps[i - 1] + v * pw1) % M
        pw1 = (pw1 * p) % M
    
    inv_pw = [1] * (N)
    inv_p = pow(p, -1, M)
    for i in range(1, N):
        inv_pw[i] = (inv_pw[i - 1] * inv_p) % M

    return ps, inv_pw

def sub_hash(M, ps, inv_pw, l, r):
    """
    Returns hash value of s[l, r] (both included) in O(1).
    M : Hash modulo
    ps : prefix hashes
    inv_pw : precomputed inverse powers of p**k (the prime ``p`` used for ``ps``)
    l : left boundary
    r : right boundary
    """
    return (ps[r] - ps[l - 1]) * inv_pw[l] % M
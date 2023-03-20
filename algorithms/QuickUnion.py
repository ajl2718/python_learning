class QuickUnion():
    """
    Implementation of QuickUnion algorithm from
    Sedgewick and Wayne Algorithms Course
    """
    def __init__(self, n):
        self.values = [k for k in range(n)]

    def root(self, i):
        while (i != self.values[i]):
            i = self.values[i]
        return i 
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.values[i] = j

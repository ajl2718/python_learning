class QuickFind():
    """
    Implementation of Quick Find data structure
    from Sedgewick and Wayne Data structures 
    course
    """
    def __init__(self, n):
        self.values = [k for k in range(n)]
    
    def union(self, i, j):
        q = self.values[j]
        p = self.values[i]
        for k in range(len(self.values)):
            if self.values[k] == p:
                self.values[k] = q

    def connected(self, i, j):
        self.values[i] == self.values[j]
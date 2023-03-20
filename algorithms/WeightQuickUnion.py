class WeightedQuickUnion:
    def __init__(self, n):
        self.values = [k for k in range(n)]
        self.size = [0 for _ in range(n)]

    def root(self, i):
        while (i != self.values[i]):
            i = self.values[i]
        return i

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if (i == j):
            return
        if (self.size[i] < self.size[j]):
            self.values[i] = j
            self.size[j] += self.size[i]
        else:
            self.values[j] = i
            self.size[i] += self.size[j]

    def connected(self, i, j):
        self.root(i) == self.root(j)


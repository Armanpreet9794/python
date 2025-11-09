class two_lines:
    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def intersection(self, other):
        D = self.a * other.b - other.a * self.b
        if D == 0:
            return None
        x = (self.c * other.b - other.c * self.b) / D
        y = (self.a * other.c - other.a * self.c) / D
        return (x, y)
    
    
import math

class Point:
    

    def distance_to(self, other):
        return math.sqrt((self.x-other.x)*2+(self.y-other.y)*2)

    def midpoint(self, other):
        return Point((self.x + other.x)/2, (self.y + other.y)/2)

    def line_equation(self, other):
        if self.x==other.x:
            return None, self.x  
        m = (other.y - self.y) / (other.x-self.x)
        c = self.y - m * self.x
        return m, c

    def reflect_over_line(self, A, B):
        if A.x == B.x:
            x_reflect = 2 * A.x - self.x
            y_reflect = self.y
            return Point(x_reflect, y_reflect)
        elif A.y == B.y:
            x_reflect = self.x
            y_reflect = 2 * A.y - self.y
            return Point(x_reflect, y_reflect)
        else:
            m, c = A.line_equation(B)
            d = (self.x + (self.y - c) * m) / (1 + m**2)
            x_reflect = 2 * d - self.x
            y_reflect = 2 * d * m - self.y + 2 * c
            return Point(x_reflect, y_reflect)
    def _repr_(self):
        return f"({self.x:.2f}, {self.y:.2f})"
    
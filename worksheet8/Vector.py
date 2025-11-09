import math

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle_with(self, other):
        dot = self.dot(other)
        mag_product = self.magnitude() * other.magnitude()
        if mag_product == 0:
            return None
        cos_theta = max(min(dot / mag_product, 1), -1)
        return math.degrees(math.acos(cos_theta))

    def projection_on(self, other):
        other_mag_sq = other.magnitude()**2
        if other_mag_sq == 0:
            return Vector(0, 0)
        scale = self.dot(other) / other_mag_sq
        return Vector(scale * other.x, scale * other.y)

    def __repr__(self):
        return f"<{self.x:.2f}, {self.y:.2f}>"

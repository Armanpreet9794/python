import math

class Segment:
    def _init_(self, start, end):
        self.start = start
        self.end = end

    def distance(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    def closest_point(self, P):
        S = self.start
        E = self.end
        SE_x = E[0] - S[0]
        SE_y = E[1] - S[1]
        length_sq = SE_x*2 + SE_y*2
        if length_sq == 0:
            return S  
        t = ((P[0] - S[0]) * SE_x + (P[1] - S[1]) * SE_y) / length_sq
        t = max(0, min(1, t))  
        closest_x = S[0] + t * SE_x
        closest_y = S[1] + t * SE_y
        return(closest_x,closest_y)
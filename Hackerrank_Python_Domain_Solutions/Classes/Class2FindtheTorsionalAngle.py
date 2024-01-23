import math

"""
Title     : Class 2 - Find the Torsional Angle
Problem   : https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
"""


class Points:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def absolute(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def cross(self, other):
        return Points(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )


if __name__ == "__main__":
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = (
        Points(*points[0]),
        Points(*points[1]),
        Points(*points[2]),
        Points(*points[3]),
    )
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))

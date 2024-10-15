class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.e = [x,y,z]
    def __repr__(self):
        return f"<Vec x:{self.x} y:{self.y} z:{self.z}>"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        self.e = [self.x, self.y, self.z]
        return Vec3(self.x, self.y, self.z)
    def __mul__(self, other):
        self.x = self.x * other
        self.y = self.y * other
        self.z = self.z * other
        self.e = [self.x, self.y, self.z]
        return Vec3(self.x, self.y, self.z)
    def __truediv__(self, other):
        self.x = self.x/other
        self.y = self.y/other
        self.z = self.z/other
        self.e = [self.x, self.y, self.z]
        return Vec3(self.x, self.y, self.z)




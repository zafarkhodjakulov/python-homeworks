import math

class Vector:
    
    def __init__(self, *args):
        self.args = args
        
    def __str__(self):
        return f"Vector{self.args}"
    
    def __add__(self, other):
        x = self.args[0] + other.args[0]
        y = self.args[1] + other.args[1]
        z = self.args[2] + other.args[2]
        return Vector( x, y, z)
    
    def __sub__(self, other):
        x = abs(self.args[0] - other.args[0])
        y = abs(self.args[1] - other.args[1])
        z = abs(self.args[2] - other.args[2])
        return Vector( x, y, z)
        
    
    def dot_product(self, other):
        x = self.args[0]*other.args[0]
        y = self.args[1]*other.args[1]
        z = self.args[2]*other.args[2]
        mul = x + y + z
        return mul
    
    def __mul__(self, a):
        x = self.args[0] * a
        y = self.args[1] * a
        z = self.args[2] * a
        return Vector(x, y, z)
    
    def magnitude(self, other):
        x = abs(self.args[0]-other.args[0])**2
        y = abs(self.args[1]-other.args[1])**2
        z = abs(self.args[2]-other.args[2])**2
        mul = math.sqrt(x + y + z)
        return mul
    
    def normalization(self, other):
        b = Vector.magnitude(self=self, other=other)
        x = self.args[0] / b
        y = self.args[1] / b
        z = self.args[2] / b
        return Vector(x, y, z)
        
  
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 7, 6)
v3 = v1 - v2
print(v3)
import geometry_msgs.msg as gm
from tf.transformations import *
import sympy
class Quaternion:
    def __init__(self, x, y, z, w):
        self.q = [x, y, z, w]
    def __add__(self, other):
        x = self[0] + other[0]
        y = self[1] + other[1]
        z = self[2] + other[2]
        w = self[3] + other[3]
        return Quaternion(x, y, z, w)
    def norm(self):
        return self[0]*self[0] + self[1]*self[1] + self[2]*self[2] + self[3]*self[3]
    def __mul__(self, other):
        x = self[3]*other[0] + self[0]*other[3] + self[1]*other[2] - self[2]*other[1]
        y = self[3]*other[1] - self[0]*other[2] + self[1]*other[3] + self[2]*other[0]
        z = self[3]*other[2] + self[0]*other[1] - self[1]*other[0] + self[2]*other[3]
        w = self[3]*other[3] - self[0]*other[0] - self[1]*other[1] - self[2]*other[2]
        return Quaternion(x, y, z, w)
    def __neg__(self):
        return Quaternion(-self[0], -self[1], -self[2], -self[3])
    def __sub__(self, other):
        x = self[0] - other[0]
        y = self[1] - other[1]
        z = self[2] - other[2]
        w = self[3] - other[3]
        return Quaternion(x, y, z, w)        
    def __getitem__(self, index):
        return self.q[index]
    def __setitem__(self, index, value):
        self.q[index] = value
    def __iter__(self):
        return iter(self.q)
    def __repr__(self):
        return repr(self.q)
    def __str__(self):
        return str(self.q)
    @property
    def x(self): return self.q[0]
    @property
    def y(self): return self.q[1]
    @property
    def z(self): return self.q[2]
    @property
    def w(self): return self.q[3]
    def conj(self):
        return Quaternion(-self[0], -self[1], -self[2], self[3])

if __name__=="__main__":
    qx, qy, qz, qw = sympy.symbols("q.x, q.y, q.z, q.w")
    v1, v2, v3 = sympy.symbols("v1, v2, v3")
    q = Quaternion(qx, qy, qz, qw)
    v = Quaternion(0, v1, v2, v3)
    rotated = q*v*q.conj()
    for item in rotated:
        print(sympy.collect(sympy.expand(sympy.simplify(item)), (v1, v2, v3)))
    for i in range(10):
        q1t = random_quaternion()
        q2t = random_quaternion()
        q1s = Quaternion(q1t[0], q1t[1], q1t[2], q1t[3])
        q2s = Quaternion(q2t[0], q2t[1], q2t[2], q2t[3])
        print(q1s*q2s-quaternion_multiply(q1t, q2t))

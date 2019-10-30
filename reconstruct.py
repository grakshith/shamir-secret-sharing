import sympy
import random

class Reconstruct():
    def __init__(self, points):
        self.points = points

    def interpolate(self):
        x = sympy.symbols('x')
        interpolated = sympy.polys.polyfuncs.interpolate(self.points, x)
        self.polynomial = sympy.polys.polytools.poly(interpolated)
        
    
    def reveal_secret(self):
        secret = self.polynomial.eval(0)
        print(secret)


if __name__ == "__main__":
    reconstruct = Reconstruct([(930, 278470440086628926944), (231, 17312419486920630658), (715, 164723819368213873034)])
    reconstruct.interpolate()
    reconstruct.reveal_secret()
    
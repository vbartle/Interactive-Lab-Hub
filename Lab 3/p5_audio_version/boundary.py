from p5 import *

class Boundary:
    def __init__(self, x1, x2, y1, y2):
        self.a = Vector(x1, y1)
        self.b = Vector(x2, y2)
    
    def show(self):
        stroke('white')
        line(self.a.x, self.a.y, self.b.x, self.b.y)

if __name__ == '__main__':
    run()
from p5 import *

class Ray:
    def __init__(self, pos, angle):
        self.pos = Vector(pos.x, pos.y)
        self.dir = Vector.from_angle(angle)

    def look_at(self, x, y):
        self.dir.x = x - self.pos.x 
        self.dir.y = y - self.pos.y
        self.dir.normalize()


    def show(self):
        stroke(100,100,255)
        with push_matrix():
            translate(self.pos.x, self.pos.y)
            line(0, 0, self.dir.x*10 , self.dir.y*10)

    def cast(self, wall):
        # start point
        x1 = wall.a.x
        y1 = wall.a.y

        # end point 
        x2 = wall.b.x
        y2 = wall.b.y

        # position of ray
        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y
        
        # denominator
        den = (x1 -x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return None
        
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (t > 0 and t < 1 and u > 0):
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            return Vector(x, y) 

        else:
            return None

if __name__ == '__main__':
    run()
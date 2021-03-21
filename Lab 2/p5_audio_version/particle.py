from p5 import *
from ray import Ray

class Particle:
    def __init__(self):
        self.pos = Vector(mouse_x, mouse_y)

    def update(self, x , y):
        self.pos = Vector(x, y)
        self.rays = []
        for a in range(0, 360, 1):
            self.rays.append(Ray(self.pos, radians(a)))

    def look(self, walls):

        for ray in self.rays:
            closest = None
            record = 1000000 
            for wall in walls:
                
                point = ray.cast(wall)
                if point:
                    d = Vector.distance(self.pos, point)
                    if d < record:
                        record = d
                        closest = point 
                    
            if closest:
                stroke('orange')
                line(self.pos.x, self.pos.y, closest.x, closest.y)



    def show(self):
        fill(255)
        ellipse((self.pos.x, self.pos.y),4, 4)
        for ray in (self.rays):
            ray.show()

if __name__ == '__main__':
    run()
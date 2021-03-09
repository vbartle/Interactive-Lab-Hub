from p5 import *
from boundary import Boundary
from particle import Particle

walls = []

def setup():
    size(800, 800)
    global particle

    for i in range(5):
        x1 = random_uniform(width)
        x2 = random_uniform(width) 
        y1 = random_uniform(width) 
        y2 = random_uniform(width)
        walls.append(Boundary(x1, y1, x2, y2))
    
    # make boundaries of edges
    walls.append(Boundary(0, 0, height, 0))
    walls.append(Boundary(height, 0, height, width))
    walls.append(Boundary(height, width, 0, height))
    walls.append(Boundary(0, width, 0, 0))

    particle = Particle()

def draw():
    background(0)

    for wall in walls:
        wall.show()
    
    particle.update(mouse_x, mouse_y)
    particle.show()
    particle.look(walls)

if __name__ == '__main__':
    run()
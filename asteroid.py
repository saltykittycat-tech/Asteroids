from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    
    def draw (self, screen):
        pygame.draw.circle(screen, "white", (self.position[0], self.position[1]), self.radius, 2)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position

    def split(self):
        old_velocity = self.velocity
        old_radius = self.radius
        x = self.position[0]
        y = self.position[1]
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_asteroid_1_velocity = old_velocity.rotate(random_angle)
        new_asteroid_2_velocity = old_velocity.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(x,y, new_radius)
        new_asteroid_2 = Asteroid(x, y, new_radius)
        new_asteroid_1.velocity = new_asteroid_1_velocity * 1.2
        new_asteroid_2.velocity = new_asteroid_2_velocity * 1.2

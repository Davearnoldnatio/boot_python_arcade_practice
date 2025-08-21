import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = self.velocity.rotate(random_angle) * 1.2
        split_2.velocity = self.velocity.rotate(-random_angle) * 1.2


        
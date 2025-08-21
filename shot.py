import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.add(*self.containers)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)
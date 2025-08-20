import pygame

class CircleShape(pygame.sprite.Sprite):
    # creating a circle used for hit detection between units
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2 (0, 0)
        self.radius = radius 

    def draw (self, screen):
        #overiden by subclasses
        pass

    def update (self, dt):
        #overiden by subclasses
        pass    
    

    
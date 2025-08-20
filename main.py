"""boot.dev practice using arcade"""

#setup
import pygame
from constants import *
from player import Player



#main
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            dt = clock.tick(60) / 1000
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        

#run
if __name__ == "__main__":
    main()

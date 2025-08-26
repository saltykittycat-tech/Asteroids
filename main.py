import pygame
from constants import *
from player import *
from AsteroidField import *
from circleshape import *
import sys

pygame.init ()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
AsteroidField.containers = (updateable)



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for thing in drawable:
            thing.draw(screen)
        updateable.update(dt)
        for asteroid in asteroids:
           if asteroid.collision_check(player) == True:
                print("Game Over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

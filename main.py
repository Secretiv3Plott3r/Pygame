# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import*
from asteroidfield import*
from Shot import *
from suplies import *
import random



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    suplie_timer = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    sup = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Suplie.containers = (sup,updatable, drawable)
    Asteroid.containers = (targets,updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot_class.containers = (bullets,updatable,drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field=AsteroidField()

    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)
        for asteroid in targets:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()
            for bullet in bullets:
                if asteroid.collisions(bullet):
                    bullet.kill()
                    asteroid.split_asteroid()
        for s in sup:
            if s.collisions(player):
                s.kill()
                player.suplie_boost()

        screen.fill((0, 0, 0))

        for dra in drawable:
            dra.draw(screen)

        pygame.display.flip()

        dt=clock.tick(60)/1000

    pygame.quit()
    

if __name__ == "__main__":
    main()
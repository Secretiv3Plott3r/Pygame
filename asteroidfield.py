import pygame
import random
from asteroid import Asteroid
from constants import *
from suplies import Suplie


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer_as = 0.0
        self.spawn_timer_sup=0.0

    def as_spawn(self, as_radius, as_position,as_velocity):
        asteroid = Asteroid(as_position.x, as_position.y, as_radius)
        asteroid.velocity = as_velocity

    def sup_spawn(self,position):
        suplie=Suplie(position.x,position.y)

    def update(self, dt):
        self.spawn_timer_as += dt
        if self.spawn_timer_as>ASTEROID_SPAWN_RATE:
            self.spawn_timer_as= 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.as_spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

        self.spawn_timer_sup += dt
        if self.spawn_timer_sup>SUPLIE_SPAWN_RATE:
            self.spawn_timer_sup= 0

            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            self.sup_spawn(pygame.Vector2(x, y)) # Se agrega automáticamente gracias a containers

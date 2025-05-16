import circleshape
import pygame
from constants import *
from Shot import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown=0
        self.bull=100

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def rotate(self,dt):
        self.rotation+= PLAYER_TURN_SPEED*dt
    
    def update(self, dt):
        self.cooldown-=dt
        keys = pygame.key.get_pressed()
    

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.cooldown > 0:
            return
        if self.bull<1:
            return "need more bullets!"
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        self.bull-=1
        new_shot=Shot_class(self.position.x,self.position.y)
        new_shot.velocity=pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SPEED

    def suplie_boost(self):
        self.bull+=50
        print("Suplie Boost!!")
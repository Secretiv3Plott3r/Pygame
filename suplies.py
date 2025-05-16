import circleshape
from constants import *
import pygame
import player

class Suplie(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SUPLIE_RADIUS)
        self.time_left=SUPLIE_TIME
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.time_left-=dt
        if self.time_left<=0:
            self.kill()

    def outta_time(self):
        return self.time_left <= 0
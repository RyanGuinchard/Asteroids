from circleshape import CircleShape
import constants as c
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, c.SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
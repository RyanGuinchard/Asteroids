from circleshape import CircleShape
import constants as c
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, c.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        # Angle the new asteroids in opposite directions
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        # Create the new asteroids with the directions
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - c.ASTEROID_MIN_RADIUS)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - c.ASTEROID_MIN_RADIUS)
        asteroid2.velocity = velocity2
        
        # Speed them up
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

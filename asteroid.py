import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, radius)

            new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2

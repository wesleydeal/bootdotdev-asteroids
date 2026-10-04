from circleshape import CircleShape
from constants import *
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20,50)

        r = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position[0], self.position[1], r)
        a2 = Asteroid(self.position[0], self.position[1], r)
        a1.velocity = self.velocity.rotate(angle) * 1.2
        a2.velocity = self.velocity.rotate(-angle) * 1.2


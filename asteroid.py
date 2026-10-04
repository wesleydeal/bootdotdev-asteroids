from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)

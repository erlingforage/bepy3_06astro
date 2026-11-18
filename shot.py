

# Lession name: 06.04.03_my_shooting
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

# solution # Lession name: 06.04.03_my_shooting
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


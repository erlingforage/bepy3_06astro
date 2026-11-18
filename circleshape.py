
# added in 06.03.01_my_sprites
import pygame


# pasted per instructions from 06.03.01_my_sprites

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # def draw(self, screen: pygame.Surface) -> None:
    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

# 06.04.02_my_collisions
# Each CircleShape has a position property that is a pygame.Vector2. You can use the position's distance_to method 
# to get the distance between the two shapes, then use that distance to decide whether to return True or False.
    def collides_with(self, other: "CircleShape") -> bool:
        # ?? why collision from start due to distance zero: 06.04.02_my_collisions
        # print(f"distance {self.position.distance_to(other.position)}")
        # print(f"my radius {self.radius}")
        # print(f"other radius {other.radius}")
        return self.position.distance_to(other.position) <= (self.radius+other.radius)

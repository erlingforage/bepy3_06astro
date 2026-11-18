


# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py
# cat filename.txt | clip.exe
# git wsl astro into github astro
# git add .
# git commit -m "message"
# git push

# 6. Build Asteroids

# ch4 Asteroids
# L1 Asteroids
# Moving
# 06.04.01_my_asteroids

# difficulty 9
# submit: bootdev run -s 
# submit: bootdev run
# submit below passed 11/6/2026
# bootdev run -s 12d26038-a9f0-4ef7-bb19-a659fc150ed0

"""
points to consider:
main.py
made assumptions about initial input into af1, a1
190 af1.spawn(ASTEROID_MIN_RADIUS,p1.position,a1.position)

84  af1 = AsteroidField()
85    a1 = Asteroid(100, 50, ASTEROID_MIN_RADIUS)


"""


"""

Submitting next lesson:
4.1 - Asteroids
Continue? [y/N]: y
✓  Check the asteroid field and spawned asteroids


All tests passed! 🎉

Gained +576 XP
+480 XP (Lesson)
+ 96 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

"""


"""
Asteroids
A critical part of Asteroids is the... well, asteroids. Let's create another class to represent them.

Asteroids in our game are simply circles.

Assignment
Create a new class called Asteroid in a new file called asteroid.py that inherits from CircleShape.

Give it a constructor with this signature, and inside it call the parent CircleShape constructor so the sprite is initialized correctly:

def __init__(self, x: float, y: float, radius: float) -> None:
    super().__init__(x, y, radius)

Override the draw() method to draw the asteroid using the pygame.draw.circle function. It accepts:

The "surface" to draw on (the screen object)

The color of the circle ("white")

Its own position as the center

Its own radius

The width of the line to draw the circle (use LINE_WIDTH from constants.py)

Override the update() method so that it moves in a straight line at constant speed. On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).

In main.py before the game loop starts, create a new empty pygame.sprite.Group for the asteroids.

Like we did with the Player class, set the static containers field of the Asteroid class to the new asteroids group, as well as the updatable and drawable groups. This ensures that every instance of the Asteroid class is automatically added to these groups upon creation.

Asteroid.containers = (asteroids, updatable, drawable)

Add the following constants to constants.py:

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

I've written an AsteroidField class for you – it contains logic for spawning new asteroids. Create a new file called asteroidfield.py and paste in this code:

import random
from collections.abc import Callable

import pygame
from asteroid import Asteroid
from constants import *

Edge = tuple[pygame.Vector2, Callable[[float], pygame.Vector2]]


class AsteroidField(pygame.sprite.Sprite):
    containers: pygame.sprite.Group

    edges: list[Edge] = [
        (
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ),
        (
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ),
        (
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ),
        (
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ),
    ]

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(
        self, radius: float, position: pygame.Vector2, velocity: pygame.Vector2
    ) -> None:
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

In the main.py file, import the AsteroidField class and set its static containers field to only the updatable group (it's not drawable, and it's not an asteroid itself).

After adding the container, create a new AsteroidField object.

Run the game for at least a few seconds, making sure that asteroids are spawning and moving across the screen, and that you didn't break your ship in the process.

If everything looks good, run and submit the CLI tests.








"""
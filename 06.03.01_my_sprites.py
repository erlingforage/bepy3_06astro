
# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py

# 6. Build Asteroids

# ch3 Player 
# L1
# Sprites

# difficulty 3
# submit: bootdev run -s a56fface-8a77-40ee-bf17-50d76078e5ec
# submit passed 11/4/2026

"""
assignments CLI tests results:

Submitting lesson:
3.1 - Sprites
✓  Check that CircleShape inherits from Sprite


All tests passed! 🎉

Gained +144 XP
+120 XP (Lesson)
+ 24 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

Tip: When you reach your next CLI lesson, you can skip copying its ID:
  bootdev run



"""

"""

Sprites
In our game, asteroids are visually represented as circles, and the player is a triangle. However, detecting collisions between circles and triangles is hard. To avoid this problem, we can cheat a bit: the player will secretly be a circle (for the purposes of collision detection).

The player is secretly a circle

The red circle won't be visible in the game; we just need to know it exists.

Throughout this project, we will provide some of the code for you, like the class below. We want you to focus on OOP concepts not the game physics. As such, we've pre-written some of the code you'll need, like the CircleShape class below.

Assignment
In Pygame, there's a base Sprite class that represents visual objects.

Let's create a CircleShape class that inherits from Sprite to represent objects in our game that are treated as circles (even if they aren't, like the player's ship).

Create a new circleshape.py file and paste in the following code:

import pygame


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

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

CircleShape extends the Sprite class to store 3 additional attributes specific to our game:

position (x and y coordinates)
velocity
radius.
Later we'll write subclasses of CircleShape and override the draw and update methods with the logic for each particular game object.

Run and submit the CLI tests from the root of the project.

"""
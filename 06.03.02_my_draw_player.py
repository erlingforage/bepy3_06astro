

# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py

# 6. Build Asteroids

# ch3 Player 
# L2
# Draw Player

# difficulty 7
# submit: bootdev run -s 
# bootdev run -s c504a055-69b9-49a9-a9cf-40a30556af92
# submit passed 11/5/26 

"""
main.y supported by

import pygame  
from logger import log_state
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH




"""



"""

Submitting next lesson:
3.2 - Draw Player
Continue? [y/N]: y
✓  Check that the player starts at the center


All tests passed! 🎉

Gained +632 XP
+360 XP (Lesson)
+ 72 XP (20%  Daily Streak)
+200 XP (Daily Bonus)

Return to your browser to continue with the next lesson.


"""

"""

Draw Player
Let's draw a spaceship for the player!

When you use a constant or class from another file (like constants.py), remember to import it at the top of your file, for example: from constants import PLAYER_RADIUS.

Assignment
Add the following values to constants.py:

PLAYER_RADIUS = 20 (the radius of the player's ship)

LINE_WIDTH = 2 (the width of the lines that draw the player's ship)

Create a new file called player.py with a Player class that inherits from CircleShape.

The Player constructor should take x and y coordinates as input, then:

Call the parent class's constructor, passing in x, y, and the PLAYER_RADIUS (you'll need to import it from your constants)

Create an attribute called rotation, initialized to 0.

Paste the triangle method below into your Player class. A player will look like a triangle, even though we'll use a circle to represent its hitbox. The math of drawing a triangle can be a bit tricky, so we've written the method for you:

# in the Player class
def triangle(self) -> list[pygame.Vector2]:
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon(). It takes as inputs:

The screen object

A color (use "white")

A list of points (use the list returned by a call to the self.triangle() function)

A line width (use the one in your constants.py file)

In your main function, instantiate a Player object. You can pass these values to the constructor to spawn it in the middle of the screen:

x = SCREEN_WIDTH / 2

y = SCREEN_HEIGHT / 2

Lastly, we need to re-render the player on the screen each frame, meaning inside our game loop. Use the player.draw(screen) method we just added to do so.

Draw the player after filling the screen with black, but before flipping the screen.

Run the game for at least a few seconds, so that the log file gets populated.

If everything worked, you should see a black screen with a white triangle in the middle. Progress! Run and submit the CLI tests.








"""
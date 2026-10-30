# difficulty 6
# bootdev run -s 268bb0d0-3e63-4218-aacc-cba3247a1af5
# passed submit 10/30/2026 
"""

Submitting next lesson:
2.1 - Modules
Continue? [y/N]: y
✓  Check the startup message and screen dimensions
✓  Check the screen constants


All tests passed! 🎉

Gained +414 XP
+300 XP (Lesson)
+ 66 XP (22%  Boots Aura)
+ 48 XP (16%  Daily Streak)

Return to your browser to continue with the next lesson.

"""

# update main.py
# create new constants.py

# uv run main.py

# after change per 06.01.03_pygame

import pygame   
# 06.02.01_my_modules
import constants
# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 720

def main():
    # after change per 06.01.03_pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print("Hello from 06class-asteroids05-wsl!")
    # 06.02.01_my_modules
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


"""

import pygame   


def main():
    # after change per 06.01.03_pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print("Hello from 06class-asteroids05-wsl!")


if __name__ == "__main__":
    main()

"""

"""

Modules
It would be a massive pain if we had to fit all of our code into a single file. So, let's organize our code into separate modules.

Since each .py file is a module, we can group related functions, variables, and classes together in a module. Then, other modules can import them using the syntax:

from module_name import my_function
# or import everything: from module_name import *

Constants
Games often have a lot of magic numbers to represent things like player speeds, item costs, and attack damage. We'll use a dedicated module as a place to store those kinds of constant values.

Assignment
Create a new file in your project called constants.py (in the same folder as main.py), and paste this in:
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

Import SCREEN_WIDTH and SCREEN_HEIGHT from the constants.py file into main.py.
Check that __pycache__/ is in your .gitignore file (create one if uv init didn't). Python creates that directory when importing your modules.
After the "Starting Asteroids..." message, also print out the SCREEN_WIDTH and SCREEN_HEIGHT values when main.py is run, using the format below:
Screen width: 1280
Screen height: 720

Run and submit the CLI tests.

"""
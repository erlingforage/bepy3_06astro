
#  /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl


"""

Pygame
Now that we have pygame installed, let's write just a bit of boilerplate code so that we have a runnable program to build on.

Assignment
Open main.py. It should have been created when you ran uv init.

On the first line, import the pygame module. This will allow us to use the pygame library in this file.

import pygame

Modify the main function from the default print statement to instead print the pygame.version.ver:

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

Keep the __name__ == "__main__" codeblock at the bottom of the file. This line ensures that the main function is called only when this file is run directly; it won't run if it's imported as a module. It's considered the "Pythonic" way to structure an executable program in Python.

Run the program with uv run main.py.

Submit the CLI tests using the Boot.dev CLI. There's no penalty on failure for this lesson.

"""
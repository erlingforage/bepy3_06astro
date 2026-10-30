# /home/erlin/asteroids05


"""

Installation
We're going to be using Pygame and a virtual environment to develop our game.

Pygame
Pygame is a module for developing games using Python. It provides simple functions and methods for us to draw images within a GUI window and handle user input.

Unfortunately, Pygame does not yet support Python 3.14. Until it's updated, we recommend using Python 3.13. uv init --no-package --python 3.13 can manage that project version for you.

Virtual Environment (venv)
Virtual environments are Python's way to keep dependencies (e.g., the pygame module) separate from other projects on our machine. For example, we need pygame version 2 for this project, but another project on your computer might require version 1.

As a best practice, each Python project on your machine should have its own virtual environment to keep things isolated.

We'll keep the game's Python files alongside main.py in the project root. If you're unsure, follow this layout. You can organize things differently, but update your imports and keep any paths required by the CLI tests.

Assignment
Create a new uv project on your computer.

uv init --no-package --python 3.13 your-project-name
cd your-project-name

--python 3.13 pins your project's Python version to 3.13

Create a virtual environment at the top level of your project directory:

uv venv

Activate the virtual environment:

source .venv/bin/activate

You should see (your-project-name) at the beginning of your terminal prompt – for example, mine is:

(Asteroids) wagslane@MacBook-Pro-2 Asteroids %

Make sure your virtual environment is activated when running the game or using the bootdev CLI.

Add the pygame library as a project dependency:

uv add pygame==2.6.1

This tells Python that this project requires pygame with an exact version of 2.6.1.

Make sure pygame is installed:

uv run -m pygame

This will result in an error (the test expects an exit code of 1), but the output will show that pygame is installed.

Submit the CLI tests. There's no penalty on failure for this lesson.

for Windows Users
If you're on WSL and pygame can't open a window, you may need to install VcXsrv. (What is VcXsrv?) Install the latest release. If you need help at any point, ask in the community Discord.


"""
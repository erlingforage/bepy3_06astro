# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl

# difficulty 5
# bootdev run -s
#

"""
Game Loop
Video games are generally built using a game loop. The simplest game loop has 3 steps:

Check for player inputs
Update the game world
Draw the game to the screen
To create a good user experience, these 3 steps need to happen many times per second.

Assignment
In main.py import the log_state function from the logger module that you created in the last assignment:
from logger import log_state

Within the main() function, initialize pygame using the pygame.init() function at the beginning of your program.
Use pygame's display.set_mode function to get a new instance of GUI window:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Create the game loop. For now, we'll only worry about step 3 from the list above: drawing the game to the screen.
Use an infinite while loop (e.g. while True:) for the game loop. At each iteration, it should:
Call log_state() – no arguments needed.
Add the following code, so that we can start processing the pygame event queue. We won't handle any events yet, we'll just call pass so our program remains responsive:
for event in pygame.event.get():
    pass

Use the screen's .fill method to fill the screen with a solid "black" color (you can literally just pass the string "black" to the method).
Use pygame's display.flip() function to refresh the screen. Be sure to call this last!
Run and test your game frequently as you write code to make sure it's working as expected. For now, you should see a black window open and stay open.
uv run main.py

Close the game and kill the program with Ctrl+C in the terminal (not the close button in the window).
In your event queue loop, if the event type is a pygame.QUIT event, return. This will check if the user has closed the window, and exit the game loop if they do. It will make the window's close button actually work.
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

Make a Git commit! It's a good idea to commit your progress whenever you get something new working.
After running the game program for a bit, then closing it, check that you have a non-empty game_state.jsonl file (but don't edit it manually). Most of the assignments for the remainder of this project will be tested against the log file.
Run and submit the CLI tests.

"""
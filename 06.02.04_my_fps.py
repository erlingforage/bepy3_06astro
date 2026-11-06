
# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py

# 6. Build Asteroids

# difficulty 5
# submit: bootdev run -s
# passed submit 10/31/2026
# bootdev run -s 658641f2-586b-48eb-bfb0-e7612cdd5dfd

"""

Continue? [y/N]: y
✓  Check elapsed time between game snapshots


All tests passed! 🎉

Gained +572 XP
+240 XP (Lesson)
+ 94 XP (39%  Boots Aura)
+ 38 XP (16%  Daily Streak)
+200 XP (Daily Bonus)

Return to your browser to continue with the next lesson.

"""


"""

FPS
As it stands, our game is re-drawing the screen as fast as it possibly can. This causes it to use a lot more CPU than it actually needs!

Delta Time
The Greek letter delta (Δ) is often used to represent a change in a value in mathematics. In game development, we use "delta time" to represent the amount of time that has passed since the last frame was drawn. This value is useful to decouple the game's speed from the speed it's being drawn to the screen.

If your computer's CPU speeds up (its speed is not constant, like a sprinter running as fast as they can), the asteroids shouldn't also speed up. Conversely, if your computer slows down, the asteroids shouldn't also slow down: they may just move less smoothly.

Assignment
FPS stands for frames per second. We're going to restrict our game to draw a maximum of 60 times per second, or 60 FPS.

After initializing pygame, but before the game loop starts, create:

A new clock object using pygame.time.Clock().
A dt variable set to 0.0.
Use 0.0 instead of 0 because dt will store a decimal number of seconds. Keeping it as a float from the start makes the type hints line up with how we'll use it later.

At the end of each iteration of the game loop, call the .tick() method on the clock object, pass it 60, and save the return value divided by 1000 into dt. The .tick() method returns the amount of time that has passed since the last time it was called: the delta time.

dt = clock.tick(60) / 1000

Print the updated dt value to the console.
Re-run the game. You should still see the same black screen, but this time it should use less of your system's resources! You should also see the dt value printed over and over to the console, it may even fluctuate a bit as your computer's CPU speed changes.
Remove the line that prints dt to the console (but leave the variable itself, we'll need it later) - it creates a lot of noise, we just wanted to see it working.
If everything is still working as you'd expect, let the game run for a few seconds so that multiple entries are written to game_state.jsonl, run and submit the CLI tests.








"""



# cd /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py
# cat filename.txt | clip.exe
# git wsl astro into github astro
# git add .
# git commit -m "message"
# cat file.name | clip.exe  # to copy the file to clipboard to be pasted into some where


# git steps in the project root to remote backend23ai
# git init (if git 1st time )

# git add .
# git commit -m "first commit"
# git branch -M main
# git config --get remote.origin.url  # to find current remote
# git remote set-url origin https://github.com/erlingforage/bepy3_06bastro.git
# if not working: git remote add origin
# git push -u origin main

# ```ts ```0


# 6. Build Asteroids

# ch4 Asteroids
# L6 Spliting
# 
# difficulty 5
# submit: bootdev run -s
# Lession name: # 06.04.06_my_spliting
# 
# on the date as submited below 
# bootdev run -s
# submit passed 11.18.2026 
# bootdev run -s 09dc2ef8-bac4-43b1-81ff-23727cc512f6
## scoop: add split() method to Asteroid class. Rotate() method is on .velocity, not on the object directly in class Asteroid. 

"""

Submitting next lesson:
4.6 - Splitting
Continue? [y/N]: y
PASS  Step 1 · Check that asteroid splitting is logged


All tests passed! 🎉

Gained +288 XP
+240 XP (Lesson)
+ 48 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

"""

"""
Splitting
In the original game of Asteroids, part of the challenge comes from the fact that larger asteroids split into smaller, faster asteroids when you shoot them. Let's support that!

Large asteroids split into two medium asteroids

Medium asteroids split into two small asteroids

Small asteroids disappear when destroyed

After splitting, the new smaller asteroids move faster.

After splitting, the new smaller asteroids move in new random directions. For example, in the diagram:

Trajectory of new asteroids, after split.

A new angle for the new asteroids is chosen at random (between 20 and 50 degrees), then the new asteroids are created and start moving in those directions.

Assignment
Instead of using asteroid.kill() in our game loop, we'll create and use a new asteroid.split() method.

Add a new .split() method to the Asteroid class. It should:

Immediately .kill() itself (think about it: this asteroid is always destroyed, but maybe we'll spawn new smaller ones, depending on its size).

If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS, just return; this was a small asteroid and we're done.

Otherwise, we need to spawn 2 new asteroids like so:

Call log_event("asteroid_split") (be sure to import log_event at the top of the file).

Call random.uniform to generate a random angle between 20 and 50 degrees (be sure to import the standard random library at the top of the file).

Call the .rotate method on the asteroid's velocity vector to create a new vector representing the first new asteroids movement.

Call the .rotate again for the second new asteroid, but this time rotate it in the opposite direction (negative angle).

Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS.

Create two new Asteroid objects at the current asteroid position with the new radius.

Set the first's .velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2.

Do the same for the second asteroid, but with the second new vector.

In the game loop in main.py, replace asteroid.kill() with asteroid.split().

Run the game and shoot some asteroids!

If things seem to be working, run and submit the CLI tests.








"""
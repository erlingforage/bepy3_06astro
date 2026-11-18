

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
# L5 Destruction
# 
# difficulty 4
# submit: bootdev run -s
# Lession name: 06.04.05_my_destruction
# 
# on the date as submited below 
# bootdev run -
# submit passed 11/18/2026
# bootdev run -s 960e1df9-33f2-4142-a9aa-c66a8f7af398
## scoop:add the code in main loop


"""

4.5 - Destruction
Continue? [y/N]: y
PASS  Step 1 · Check that asteroid hits are logged


All tests passed! 🎉

Gained +216 XP
+180 XP (Lesson)
+ 36 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

"""

"""

Destruction
Okay, so bullets are flying, but they don't do anything. Let's kill some asteroids!

There are three types of asteroids:

Large

Medium

Small

When a large asteroid is destroyed, it should split into two medium asteroids. When a medium asteroid is destroyed, it should split into two small asteroids. When a small asteroid is destroyed, it should disappear.

For now, we'll just always make the asteroids disappear when they're destroyed. We'll handle splitting later.

Assignment
Add another collision check to the game loop. Loop over each asteroid, and for each asteroid, loop over each shot. If a shot and an asteroid collide:

Call log_event("asteroid_shot").

Call the .kill() method on both objects (the shot and the asteroid) to remove them from the game.

The kill() method is a built-in feature of Pygame sprites. It removes the "killed" object from all its groups so that the engine stops updating and drawing it.

Run the game for at least a few seconds, and make sure you can destroy asteroids by shooting them.

If everything looks right, run and submit the CLI tests.


"""

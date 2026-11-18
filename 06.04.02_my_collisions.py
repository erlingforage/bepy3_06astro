

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
# L2 Colliions
# 
# difficulty 6
# submit: bootdev run -s 
# submit: bootdev run
# submit below passed 11/16/2026
# Lession name: 06.04.02_my_collisions
# bootdev run -s 482925e6-e043-43a4-b9c6-9eda414bb9a7




"""

Submitting lesson:
4.2 - Collisions
✓  Check that one player collision is logged


All tests passed! 🎉

Gained +432 XP
+360 XP (Lesson)
+ 72 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

Tip: When you reach your next CLI lesson, you can skip copying its ID:
  bootdev run

"""


"""

Collisions
You may have noticed that you can fly through asteroids without any consequences.

We need collision detection. Now, this is a fairly deep topic, but we're going to keep things simple: we'll treat everything (including our triangular ship) as a circle when it comes to collisions.

Detecting a collision between two circles is simple:

Calculate the distance between the center of the two circles: "distance"

Calculate the radius of each circle: r1 and r2.

If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren't!

Demonstration of two circles colliding.

Assignment
Everything that collides inherits from CircleShape, so that seems like a good place to write our collision logic. We also want to log when collisions happen, so we'll use one more function from that logger.py module.

Add a collides_with(self, other) method to CircleShape to check for collisions. It should take another circle shape as a parameter (aside from self of course) and return True or False.

Each CircleShape has a position property that is a pygame.Vector2. You can use the position's distance_to method to get the distance between the two shapes, then use that distance to decide whether to return True or False.

Back in your main file, import the log_event function from the logger module.

Add game_events.jsonl to your .gitignore file.

After the "update" step in your game loop, iterate over all the objects in your asteroids group. Check if any of them collide with the player. If a collision is detected:

Call log_event("player_hit").

Print Game over! to the console.

End the game immediately with sys.exit(). (Don't forget to import sys!)

Start the game, and run your ship into an asteroid! It should print Game over! to your console and exit.

It's okay for asteroids to simply pass through each other for now.

If that worked, run and submit the CLI tests.

"""

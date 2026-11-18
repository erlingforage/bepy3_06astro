
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
# L3 Shooting
# 
# difficulty 9
# submit: bootdev run -s
# Lession name: 06.04.03_my_shooting
# 
# on the date as submited below 
# bootdev run -
# submit passed after solution seen and player.py shoot SHOT_RADIUS added 11.18.2026 


"""

Submitting next lesson:
4.3 - Shooting
Continue? [y/N]: y
PASS  Step 1 · Check that shots are spawned


All tests passed! 🎉

Gained +776 XP
+480 XP (Lesson)
+ 96 XP (20%  Daily Streak)
+200 XP (Daily Bonus)

Return to your browser to continue with the next lesson.

"""

"""

Shooting
Let's make things more interesting by allowing the player to shoot at the asteroids.

"Oh man. What are you doing with a gun in space?" - Armageddon (1998)

In our game, bullets:

Are small circles

Move at a constant speed in a straight line

Split up asteroids when they collide with them

Are spawned by player input (spacebar) and move in the direction the player is facing

Assignment
In constants.py, add a new SHOT_RADIUS constant and set it to 5.

Create a new Shot class to represent a bullet in a new shot.py file.

It should inherit from CircleShape, similar to the Asteroid class.

Create an __init__ method that accepts x and y. It should call the parent class's __init__ method with x, y, and the SHOT_RADIUS.

Override its draw and update methods, just like you did in the Asteroid class.

Set up a new shots group in your main.py initialization code.

Set the containers field of the Shot class to include your new shots group, along with the drawable and updatable containers, just like you did with your Player and Asteroid classes.

Add PLAYER_SHOOT_SPEED to your constants file, with a value of 500.

In your Player class, add a new method called shoot. This method takes no parameters and does the following:

Creates a new Shot at the current position of the player.

Sets the shot's .velocity attribute:

Start with a pygame.Vector2 of (0, 1).

.rotate() the vector in the direction the player is facing.

Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster.

In Player.update in player.py, handle the spacebar (pygame.K_SPACE) and call the shoot method when it's pressed.

Run your game for at least a few seconds, and fire some shots. Make sure the bullets are being created and moving in the correct direction.

It's expected that holding the spacebar will create a constant stream of bullets. We'll fix that soon.

It's expected that bullets pass through asteroids without any consequences. We'll fix that soon, too.

If everything looks right, run and submit the CLI tests.

"""
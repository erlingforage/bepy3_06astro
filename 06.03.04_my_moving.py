

# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py
# cat filename.txt | clip.exe

# 6. Build Asteroids

# ch3 Player 
# L4
# Moving
# 06.03.04_my_moving

# difficulty 4
# submit: bootdev run -s 
# submit: bootdev run
# submit passed 11/6/2026
# bootdev run -s f3c2de4d-3646-42c0-8639-71f0c4c01eaa

# but cannot do as suggested below
# You should now be able to fly around the screen with the W, A, S, and D keys!
# 06.03.04_my_moving  11/6/2026
# unless 
#  ## p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
# is before the loop


"""

Submitting next lesson:
3.4 - Moving
Continue? [y/N]: y
✓  Check that the player moves


All tests passed! 🎉

Gained +216 XP
+180 XP (Lesson)
+ 36 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

"""

"""

Moving
Now we want the ship to move back and forth with the W and S keys.

Assignment
Create a new constant in constants.py to represent the player speed called PLAYER_SPEED, and give it a value of 200.

Add a new method to the Player class called .move(). If you get stuck, use the reference below. This method takes one argument: dt. It will modify the player's position using the following math:

Start with a unit vector pointing straight down from (0, 0) to (0, 1).

Rotate that vector by the player's rotation, so it's pointing in the same direction as the player.

Import the PLAYER_SPEED constant and multiply the vector by PLAYER_SPEED * dt so that the vector is the length the player should move during this frame.

Add the vector to the player's position to move them.

This is a course on programming, not vector math, so we've provided the math for you. All those words boil down to these lines of code:

unit_vector = pygame.Vector2(0, 1)
rotated_vector = unit_vector.rotate(self.rotation)
rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
self.position += rotated_with_speed_vector

unit_vector.rotate() returns a new vector – it doesn't modify the original. That's why we assign the result to rotated_vector.

Vector Math

Modify the update method in the Player class to call the move method when the W or S key is pressed. Remember to negate dt for the S key, so the player moves backward.

Run the game for at least a few seconds. You should now be able to fly around the screen with the W, A, S, and D keys!

If everything looks good, run and submit the CLI tests.

"""


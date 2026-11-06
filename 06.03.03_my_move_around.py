


# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py
# cat filename.txt | clip.exe

# 6. Build Asteroids

# ch3 Player 
# L3
# Moving Around

# difficulty 6
# submit: bootdev run -s ca7e42fb-9493-4732-b5db-4dc0379307fd
# submit: bootdev run
# submit passed 11/6/2026

"""

Submitting lesson:
3.3 - Moving Around
✓  Check that the player rotates


All tests passed! 🎉

Gained +360 XP
+300 XP (Lesson)
+ 60 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

Tip: When you reach your next CLI lesson, you can skip copying its ID:
  bootdev run

"""


"""

Moving Around
We want the spaceship to be able to move; but what does that mean specifically? Let's break it down:

If we press the move-left key, the ship should rotate to the left (i.e., counter-clockwise).

If we press the move-right key, the ship should rotate to the right (i.e., clockwise).

If we press the move-forward key, the ship should move forward.

If we press the move-backward key, the ship should move backward.

Left and right seem pretty similar. Let's try to write a small function to tackle those first!

Assignment
Create a new constant in constants.py to represent the player's turn speed. I named mine PLAYER_TURN_SPEED, and give it a value of 300.

Add a new rotate method to the Player class. It takes one argument: dt (I told you we'd use it!). When it's called, it should add PLAYER_TURN_SPEED * dt to the player's current rotation.

Paste in the following update method to the Player class:

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
        if keys[pygame.K_d]:
            # ?

If you're using a non-QWERTY keyboard, you may want to change the keybindings in the code to something other than the W, A, S and D keys.

Update the missing lines to call the rotate method with the dt argument. To go left instead of right when a is pressed, you'll need to reverse dt... how can you do that...?

Hook the update method into the game loop by calling it on the player object each frame before rendering.

Run the game for at least a few seconds, and make sure the a and d keys rotate the player left and right, respectively.

If everything seems to be working, run and submit the CLI tests.

"""
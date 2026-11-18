

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
# L4 Rate Limit
# 
# difficulty 4
# submit: bootdev run -s
# Lession name: 06.04.04_my_rate_limit
# 
# on the date as submited below 
# bootdev run -
# submit passed 11/18/2026
## scoop: the bullets now is one by one, instead of a string of bullets when shooting

"""
Submitting next lesson:
4.4 - Rate Limit
Continue? [y/N]: y
PASS  Step 1 · Check that shooting respects the cooldown


All tests passed! 🎉

Gained +216 XP
+180 XP (Lesson)
+ 36 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

"""


"""
Rate Limit
You probably noticed that the weapon on the ship is currently as overpowered as the original Zerg rush. Let's fix that.

Assignment
In Player.__init__ in player.py, add a shot cooldown timer, such as self.shoot_timer, starting at 0.

In constants.py, create PLAYER_SHOOT_COOLDOWN_SECONDS and set it to 0.3. Import it into player.py.

At the start of Player.shoot, before creating a shot:

If the current value of the timer is greater than 0, return without shooting.

Otherwise, set the timer equal to PLAYER_SHOOT_COOLDOWN_SECONDS.

In Player.update, decrease the shoot timer by dt (the change in time) every frame, before handling the spacebar input.

Run your game for at least a few seconds, shooting to your heart's content. You should now be rate-limited to one shot every 0.3 seconds.

Bullets should still pass through asteroids without any consequences. We'll fix that soon.

If things seem to be working, run and submit the CLI tests.








"""
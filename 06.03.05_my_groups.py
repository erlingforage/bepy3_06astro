


# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py
# cat filename.txt | clip.exe
# git wsl astro into github astro
# git add .
# git commit -m "message"
# git push

# 6. Build Asteroids

# ch3 Player 
# L4
# Moving
# 06.03.05_my_groups

# difficulty 6
# submit: bootdev run -s 
# submit: bootdev run
# submit passed 11/06/2026


"""

ubmitting next lesson:
3.5 - Groups
Continue? [y/N]: y
✓  Check that updatable and drawable groups contain sprites


All tests passed! 🎉

Gained +360 XP
+300 XP (Lesson)
+ 60 XP (20%  Daily Streak)

Return to your browser to continue with the next lesson.

"""


"""

Groups
We're manually calling .update() and .draw() on the player object at the moment, which means our game loop is going to get more and more cluttered as we add additional objects to the game. Fortunately, Pygame has a solution!

The Group class is a container that holds and manages multiple game objects. We can organize our objects into various groups to track them more easily.

You can think of them as a sort of Venn diagram. An object can be in multiple groups at the same time! Eventually, our game's groups will look something like this:

Venn-diagram of the groups we will eventually have

The player needs updating and drawing, but some later objects only need updating.

Examples of Using Groups
Create a new empty group called my_group:

my_group = pygame.sprite.Group()

Add all future instances of a Player class to two different groups (group_a and group_b):

# Player is the name of the class, not an instance of it
# This must be done before any Player objects are created
Player.containers = (group_a, group_b)

You can iterate over objects in a group just like any other collection in Python:

for thing in group:
    thing.do_something(some_value)

You may also call the .update() method for every member of a group by calling it on the group itself:

group.update(dt)

Assignment
Before the game loop starts, create two new empty groups in main.py:

updatable – this will hold all the objects that can be updated

drawable – this will hold all the objects that can be drawn

Add the Player class to the updatable and drawable groups before the player object instance is created.

Player.containers = (updatable, drawable)

Update the game loop to use the new groups instead of the Player object directly.

Call the .update() method on the "updatable" group.

Loop over all "drawables" and .draw() them individually.

Run the game for at least a few seconds. It should look and behave the same as before, but now we're using groups to manage our objects.

If everything seems to be working, run and submit the CLI tests.

"""
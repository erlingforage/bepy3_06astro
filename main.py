
# cd /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
# uv run main.py


# after change per 06.01.03_pygame

import pygame   
# 06.02.01_my_modules
## import constants
# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 720


# 06.02.03_my_game_loop
from logger import log_state

# 06.03.02_my_draw_player
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
# L06.04.03_my_shooting
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS


# 06.04.01_my_asteroids
# from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField 

# L06.04.03_my_shooting
from shot import Shot

# 06.04.02_my_collisions
# from logger import log_event
# solution
# from logger import log_state

# 06.04.02_my_collisions
from logger import log_event
import sys

def main():
    pygame.init()

# after change per 06.01.03_pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print("Hello from 06class-asteroids05-wsl!")
    # 06.02.01_my_modules
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")





    # solution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # mine missing a bracket screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
    clock = pygame.time.Clock()

    # 06.03.02_my_draw_player 
    # pygame.init()

    # 06.03.05_my_groups
    # Before the game loop starts, create two new empty groups in main.py:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # 06.04.01_my_asteroids
    asteroids = pygame.sprite.Group()

    # L06.04.03_my_shooting
    # Set up a new shots group in your main.py initialization code.
    shots = pygame.sprite.Group()

    # 06.04.01_my_asteroids
    # solution
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    af1 = AsteroidField()
    Player.containers = (updatable, drawable)

    # L06.04.03_my_shooting
    # 4 Set the containers field of the Shot class to include your new shots group, 
    # along with the drawable and updatable containers, just like you did with your Player and Asteroid classes.
    Shot.containers = (shots, updatable, drawable)

    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    dt = 0.0

    


    
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

# 06.04.02_my_collisions
        for grp in asteroids:
            
            grp.update(dt)
            if grp.collides_with(p1):
                log_event("player_hit")
                print("Gamve Over!")
                sys.exit() 
# 06.04.05_my_destruction
            for shot in shots:   
                if shot.collides_with(grp):
                    log_event("asteroid_shot") 
                    # grp.kill()
                    shot.kill()     
                    # 06.04.06_my_spliting
                    # 3.9 In the game loop in main.py, replace asteroid.kill() with asteroid.split().
                    grp.split()
               

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


   


    
        
        

  

    



if __name__ == "__main__":
    main()




"""

# before change per 06.01.03_pygame

def main():
    print("Hello from 06class-asteroids05-wsl!")


if __name__ == "__main__":
    main()


"""

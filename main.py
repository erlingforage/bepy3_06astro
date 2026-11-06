
# /mnt/c/users/erlin/documents/bootdev/back_dev/py3/06class_asteroids05_wsl
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


def main():

    # 06.03.02_my_draw_player
    pygame.init()

    # after change per 06.01.03_pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print("Hello from 06class-asteroids05-wsl!")
    # 06.02.01_my_modules
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # 06.02.03_my_game_loop
    ## pygame.init()
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # 06.03.02_my_draw_player
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("blue")
    # 06.03.02_my_draw_player
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface.fill("black")
    

    # 06.02.04_my_fps
    myclock = pygame.time.Clock()
    dt = 0.0

     # 06.03.02_my_draw_player
    # Need screen.blit(surface,(0, 0)) to draw on
    # screen.blit(surface,(0, 0))
    
    # 06.03.02_my_draw_player
        # p1 = Player()
        # p1.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

        #print(f"p1.position is {p1.position}")
        # p1.position is [640, 360]


    # 06.03.02_my_draw_player
    ## running = True
    ## while running:
    
    # 06.02.03_my_game_loop
    # 06.03.03_my_move_around requires loop bool True
    while True:
        # 06.03.02_my_draw_player
        ## pygame.init()
        
        log_state()

        ## pygame.init()

        # for event in pygame.event.get():
        #    pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               ## running = False 
               # 06.02.03_my_game_loop
               # 06.03.03_my_move_around requires loop bool True
               return

        #screen.fill("blue")

        # 06.03.02_my_draw_player
        # triangle will not show if screen/surface put here
        # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # screen.fill("blue")
        # pygame.Surface.fill("black")
         # 06.03.02_my_draw_player
        # surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        # surface.fill("black")

        # 06.03.02_my_draw_player
        # Need screen.blit(surface,(0, 0)) to draw on
        screen.blit(surface,(0, 0))

# 06.03.02_my_draw_player
        # p1 = Player()
        # p1.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
        ## p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

        ## print(f"p1.position is {p1.position}")
        ## p1.position is [640, 360]


        # 06.02.04_my_fps
        dt = myclock.tick(60) / 1000
        # 06.02.04_my_fps
        ## print(f"dt: {dt}")
 
         # 06.02.03_my_game_loop
        ## screen.display.flip()

        # 06.03.02_my_draw_player
        """
        # In your main function, instantiate a Player object. You can pass these values to the constructor to spawn it in the middle of the screen:
    
            x = SCREEN_WIDTH / 2
    
            y = SCREEN_HEIGHT / 2
        """

        
        ## p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
        ## p1.draw(surface, "white", LINE_WIDTH)
        p1.draw(surface)
        

        # 06.03.03_my_move_around
        # Hook the update method into the game loop by calling it on the player object each frame before rendering.
        p1.update(dt)
        p1.draw(surface) # redraw the new location to show the move result

        

        # Draw the player after filling the screen with black, but before flipping the screen.
        # 11/6/26 pygame.display.flip() did not work
        # surface.flip() didnt work
        # # 06.03.03_my_move_around
        # triangle seen when below pygame.display.flip() inside while screen/surfact outside the loop
        pygame.display.flip()
    pygame.quit()



    



if __name__ == "__main__":
    main()




"""

# before change per 06.01.03_pygame

def main():
    print("Hello from 06class-asteroids05-wsl!")


if __name__ == "__main__":
    main()


"""

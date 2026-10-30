
# after change per 06.01.03_pygame

import pygame   
# 06.02.01_my_modules
import constants
# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 720

# 06.02.03_my_game_loop
from logger import log_state


def main():
    # after change per 06.01.03_pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print("Hello from 06class-asteroids05-wsl!")
    # 06.02.01_my_modules
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # 06.02.03_my_game_loop
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        log_state()


        # for event in pygame.event.get():
        #    pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

    screen.display.flip()



if __name__ == "__main__":
    main()




"""

# before change per 06.01.03_pygame

def main():
    print("Hello from 06class-asteroids05-wsl!")


if __name__ == "__main__":
    main()


"""

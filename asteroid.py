# 06.03.02_my_draw_player

import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED
# 06.03.04_my_moving
from constants import PLAYER_SPEED



# 06.04.01_my_asteroids



"""

Create a new class called Asteroid in a new file called asteroid.py that inherits from CircleShape.

Give it a constructor with this signature, and inside it call the parent CircleShape constructor so the sprite is initialized correctly:

def __init__(self, x: float, y: float, radius: float) -> None:
    super().__init__(x, y, radius)


"""
# solution asterods spawning 11/10/2026

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
# 06.04.06_my_spliting
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random





class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

# 06.04.06_my_spliting
    def split(self) -> None:
        # 1. Immediately .kill() itself (think about it: this asteroid is always destroyed, 
        # but maybe we'll spawn new smaller ones, depending on its size).
        self.kill()
        # 2. If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS, just return; this was a small asteroid and we're done.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # 3. Otherwise, we need to spawn 2 new asteroids like so:
        else:
           # 3.1 Call log_event("asteroid_split") (be sure to import log_event at the top of the file). 
            log_event("asteroid_split")
            # 3.2 Call random.uniform to generate a random angle between 20 and 50 degrees 
            # (be sure to import the standard random library at the top of the file).
            angle = random.uniform(20.0, 50.0)
# 3.3 Call the .rotate method on the asteroid's velocity vector to create a new vector representing the first new asteroids movement.
            vector1 = self.velocity.rotate(angle)
            angle = random.uniform(20.0, 50.0)
# 3.4 Call the .rotate again for the second new asteroid, but this time rotate it in the opposite direction (negative angle).
            vector2 = self.velocity.rotate(-angle)
            # 3.5 Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS.
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # 3.6 Create two new Asteroid objects at the current asteroid position with the new radius.
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            # 3.7 Set the first's .velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2.
            asteroid1.velocity = vector1 * 1.2
            # 3.8 Do the same for the second asteroid, but with the second new vector.
            asteroid2.velocity = vector2 * 1.2
     


"""
# my asteriods do not sprawn

# 06.04.01_my_asteroids
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)


# 06.04.01_my_asteroids
    def draw(self, surface: pygame.Surface) -> None:
               
        self.surface = surface
        self.color = "white" # ok working 11/6/26
        # self.position 
        # self.radius
        self.width = LINE_WIDTH
        pygame.draw.circle(self.surface,self.color,self.position,self.radius,self.width)

 # 06.04.01_my_asteroids
 # it moves in a straight line at constant speed. On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).   
    def update(self, dt: float) -> None:
            astro_velocity = self.velocity
            
            # keys W,S,A,D forward, backword, left, and right


            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:  <<< ===== this caused not spawning
                self.position += astro_velocity * (-dt)
            
"""



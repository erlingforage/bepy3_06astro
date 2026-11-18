
# 06.03.02_my_draw_player

import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED
# 06.03.04_my_moving
from constants import PLAYER_SPEED
# L06.04.03_my_shooting
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS
from shot import Shot

# 06.04.04_my_rate_limit
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x,y, PLAYER_RADIUS)
        self.x = x
        self.y = y
# # 06.03.04_my_moving
# testing position
        # self.position = (x,y)

        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.line_width = LINE_WIDTH
# 06.04.04_my_rate_limit
# n Player.__init__ in player.py, add a shot cooldown timer, such as self.shoot_timer, starting at 0.
        self.shoot_timer = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
# # 06.03.04_my_moving
# testing position
        # print(f"my position is {self.position}")

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # 06.03.02_my_draw_player
    # override the draw method
    # def draw(self, screen: pygame.Surface) -> None:
    def draw(self, surface: pygame.Surface) -> None:
        # # 06.03.03_my_move_around
        # why triangel not showing?
        

        self.surface = surface
        self.color = "white" # ok working 11/6/26
        # self.points = points
        self.width = LINE_WIDTH
    # 06.03.03_my_move_around

        pygame.draw.polygon(self.surface, self.color, self.triangle(), self.width)

    # 06.03.03_my_move_around
    # When it's called, it should add PLAYER_TURN_SPEED * dt to the player's current rotation.
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # 06.03.03_my_move_around
    # Paste in the following update method to the Player class:
    # Update the missing lines to call the rotate method with the dt argument. To go left instead of right when a is pressed, you'll need to reverse dt.
    # https://www.pygame.org/docs/ref/key.html
    def update(self, dt: float) -> None:
        # keys W,S,A,D forward, backword, left, and right

        keys = pygame.key.get_pressed()

        ## if keys[pygame.K_a]:
            # ?
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
            
        ## if keys[pygame.K_d]:
            # ?    
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
# 06.03.04_my_moving
        if keys[pygame.K_UP]:
            self.move(dt)  # up is negative
        if keys[pygame.K_DOWN]:
            self.move(-dt)
# 06.04.04_my_rate_limit
# 4. In Player.update, decrease the shoot timer by dt (the change in time) every frame, before handling the spacebar input.       
        self.shoot_timer -= dt     
# L06.04.03_my_shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    # 06.03.04_my_moving
    # Add a new method to the Player class called .move(). 
    # If you get stuck, use the reference below. This method takes one argument: dt. It will modify the player's position using the following math:
    def move(self, dt: float) -> None:

        # This is a course on programming, not vector math, so we've provided the math for you. All those words boil down to these lines of code:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # L06.04.03_my_shooting
    # 6. In your Player class, add a new method called shoot. This method takes no parameters and does the following:

    # 6.1 creates a new Shot at the current position of the player

# solution L06.04.03_my_shooting
#  
    def shoot(self) -> None:
# 06.04.04_my_rate_limit
    # 3. At the start of Player.shoot, before creating a shot:
    # 3.1 If the current value of the timer is greater than 0, return without shooting.
    # 3.2 Otherwise, set the timer equal to PLAYER_SHOOT_COOLDOWN_SECONDS.
        if self.shoot_timer > 0.0:
            return
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
    #  L06.04.03_my_shooting solution  
        # solution shot = Shot(self.position.x, self.position.y)
        # 6.1 Creates a new Shot at the current position of the player
        # it is working after adding radius of SHOT_RADIUS 11.18.2026
        shot = Shot(self.position.x, self.position.y, self.radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


"""

    def shoot() -> None:
        # 6.1 Creates a new Shot at the current position of the player
        shot_at_player = Shot(Player.position.x, Player.postion.y, SHOT_RADIUS)
       # 6.2 Sets the shot's .velocity attribute:
            # Start with a pygame.Vector2 of (0, 1).
        start = pygame.Vector2(0,1)
            # .rotate() the vector in the direction the player is facing.
        rotated_vector = start.rotate(Player.rotation)
            # Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster.
        shot_at_player.velocity += rotated_vector * PLAYER_SHOOT_SPEED
"""

           
        

"""

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

"""
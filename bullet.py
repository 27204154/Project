import stddraw
from math import sin, cos

# Bullet Constants
BULLET_SIZE = 5
BULLET_VELOCITY = 4


class Bullet:
    """
    Creates Bullet class for modularity, and to be reused by the Player and enemies.
    The Bullet class also contains the move_bullet function, which allows each individual bullet to move.
    {27204154, John-Robert Upton}
    """

    def __init__(self, xpos, ypos, angle):
        self.xpos = xpos
        self.ypos = ypos
        self.x_move_dist = BULLET_VELOCITY * cos(angle)
        self.y_move_dist = BULLET_VELOCITY * sin(angle)
        stddraw.filledCircle(self.xpos, self.ypos, BULLET_SIZE)

    def move_bullet(self):
        """
        Moves the bullet according to its angle, and re-draws the bullet.
        {27204154, John-Robert Upton}
        """
        self.xpos += self.x_move_dist
        self.ypos += self.y_move_dist
        stddraw.filledCircle(self.xpos, self.ypos, BULLET_SIZE)

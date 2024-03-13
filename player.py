import stddraw

# Player Constants
PLAYER_SIZE = 20
PLAYER_VELOCITY = 2


class Player:
    """
    Create Player class for modularity and to reduce clutter in main() function.
    Player class also contains functions for movement and rotation.
    {27204154, John-Robert Upton}
    """

    def __init__(self):
        self.xpos = 0
        self.rotate = 0
        self.update_player()

    def m_left(self):
        """
        Creates new player model at [constant units] left to its previous position.
        {27204154, John-Robert Upton}
        """
        self.xpos -= PLAYER_VELOCITY
        self.update_player()

    def m_right(self):
        """
        Creates new player model at [constant units] right to its previous position.
        {27204154, John-Robert Upton}
        """
        self.xpos += PLAYER_VELOCITY
        self.update_player()

    def r_left(self):
        """
        Creates new player model rotated [constant units] left to its previous position.
        {27204154, John-Robert Upton}
        """
        pass

    def r_right(self):
        """
        Creates new player model rotated [constant units] right to its previous position.
        {27204154, John-Robert Upton}
        """
        pass

    def update_player(self):
        """
        Draws player model at current x-position.
        {27204154, John-Robert Upton}
        """
        stddraw.filledCircle(self.xpos, -150, PLAYER_SIZE)

import stddraw, math
from player import Player
from bullet import Bullet

# Constants
# Game Constants
GAME_SPEED = 20
# Player Constants
PLAYER_BOUNDS = 165
# Bullet Constants
BULLET_BOUNDS_X = 200
BULLET_BOUNDS_Y = 200

# Test Comment


def main():

    screen_settings()

    # Initiates Player obj ect, and displays it at its current coordinates.
    player = Player()
    stddraw.show(GAME_SPEED)

    # Create bullets array for Bullet objects. {27204154}
    bullets = []

    key = 's'
    while not key == 'x':
        stddraw.clear()

        # Finds the next key pressed, adds bullet object to bullet array if 'fire' button is pressed. {27204154}
        # Prior key is there so that player does not stop when bullet is fired. {27204154}
        if stddraw.hasNextKeyTyped():
            prior_key = key
            key = stddraw.nextKeyTyped()
            if key == ' ':
                bullets.append(Bullet(player.xpos, -150, 0.5 * math.pi))
                key = prior_key

        # If the player clicks the 'a' of 'd' button, the player object's x position will change,
        # otherwise the player will stop moving (exception to space character). {27204154}
        elif key == 'a':
            if not player.xpos <= - PLAYER_BOUNDS:
                player.m_left()
        elif key == 'd':
            if not player.xpos >= PLAYER_BOUNDS:
                player.m_right()

        # Moves/Removes each of the bullet objects, and sets the player object at its position,
        # and shows the screen. {27204154}
        bullets = edit_bullets(bullets)
        player.update_player()
        stddraw.show(GAME_SPEED)


def screen_settings():
    """
    Prepares Screen Size, and reduces main() function clutter.
    {27204154, John-Robert Upton}
    """
    stddraw.setCanvasSize(600, 600)
    stddraw.setXscale(-200, 200)
    stddraw.setYscale(-200, 200)


def edit_bullets(bullet_array):
    """
    Moves every bullet, and checks whether each bullet is out of bounds, and removes it from the array.
    {27204154, John-Robert Upton}
    """
    out_of_bounds = []
    # Moves each bullet, checks the bounds, and adds it to out_of_bounds array.
    for bullet in bullet_array:
        if (math.fabs(bullet.ypos) > BULLET_BOUNDS_Y) or (math.fabs(bullet.xpos) > BULLET_BOUNDS_X):
            out_of_bounds.append(bullet)
        bullet.move_bullet()

    # Removes the bullets which are out of bounds from the bullets_array. {27204154}
    for bullet in out_of_bounds:
        bullet_array.remove(bullet)
        del bullet

    # Returns the updated bullets_array
    return bullet_array


if __name__ == '__main__': main()

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 100 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    Function: Brick Breaking Game.
    """
    # Turn on preparation mode
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES

    while True:
        if graphics.get_ball_outside():
            num_lives -= 1
            if num_lives > 0:
                graphics.ball_rest()
            else:
                break
        if graphics.brick_number == 0:
            break
        graphics.ball_move()
        graphics.ball_rebound_window()
        graphics.ball_rebound_obj()
        pause(FRAME_RATE)

    print('Game over')



    # Add animation loop here!


if __name__ == '__main__':
    main()

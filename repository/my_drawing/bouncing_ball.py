"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

cont = 0
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(star_ball)


def star_ball(mouse):
    """
    Function: After clicking, execute ball movement
    Principle: Use parameters to move x and y axes
    """
    global cont
    if ball.x == START_X and cont < 3:
        vel_x = VX
        vel_y = 0
        while ball.x <= window.width:
            ball.x += vel_x

            vel_y += GRAVITY
            if ball.y >= window.height:
                vel_y *= -0.9
            ball.y += vel_y

            window.add(ball)
            pause(DELAY)

        ball.x = START_X
        ball.y = START_Y
        window.add(ball)
        cont += 1




if __name__ == "__main__":
    main()

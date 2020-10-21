"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Width of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        """
        Function: Create initial parameters such as window, ball, paddle,brick etc.
        :param ball_radius: Radius of the ball (in pixels).
        :param paddle_width: Width of the paddle (in pixels).
        :param paddle_height: Height of the paddle (in pixels).
        :param paddle_offset: Vertical offset of the paddle from the window bottom (in pixels).
        :param brick_rows:  Number of rows of bricks.
        :param brick_cols: Number of cols of bricks.
        :param brick_width: Width of a brick (in pixels).
        :param brick_height: Height of a brick (in pixels).
        :param brick_offset: Vertical offset of the topmost brick from the window top (in pixels).
        :param brick_spacing: Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
        :param title: Window title
        """
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        print('dxdy')

        # Initialize our mouse listeners.
        self.brick_number = brick_rows * brick_cols
        # Draw bricks.
        self.__brick_site(brick_rows, brick_cols, brick_width, brick_height, brick_offset, brick_spacing)
        onmouseclicked(self.star_fire)
        onmousemoved(self.__move_paddle)

        self.star_switch = False
        self.ball_rest()

    def star_fire(self, mouse):
        """
        Function: When you click the mouse, start the bool.
        :param mouse: Mouse parameters
        """
        self.star_switch = True

    def __brick_site(self, b_r, b_c, b_w, b_h, b_offset, b_spacing):
        """
        Function: Establish the position of the brick
        :param b_r: Number of rows of bricks.
        :param b_c: Number of cols of bricks.
        :param b_w: Width of a brick (in pixels).
        :param b_h: Height of a brick (in pixels).
        :param b_offset: Vertical offset of the topmost brick from the window top (in pixels).
        :param b_spacing: Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
        """
        dy = b_offset
        for j in range(b_r):
            dx = 0
            for i in range(b_c):
                self.brick = GRect(b_w, b_h, x=dx, y=dy)
                self.brick.filled = True

                if j == 0 or j == 1:
                    self.brick.fill_color = 'darkgreen'
                elif j == 2 or j == 3:
                    self.brick.fill_color = 'forestgreen'
                elif j == 4 or j == 5:
                    self.brick.fill_color = 'green'
                elif j == 6 or j == 7:
                    self.brick.fill_color = 'limegreen'
                elif j == 8 or j == 9:
                    self.brick.fill_color = 'lime'
                else:
                    self.brick.fill_color = 'lawngreen'

                self.window.add(self.brick)
                dx += b_w + b_spacing
            dy += b_h + b_spacing

    def __move_paddle(self, mouse):
        """
        Function: When moving the mouse, move the position of the paddle.
        :param mouse: Mouse parameters
        """
        if (mouse.x <= self.window.width - self.paddle.width/2) and (mouse.x >= self.paddle.width/2):
            self.paddle.x = mouse.x - (self.paddle.width/2)
        elif mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def set_ball_velocity(self):
        """
        Function: set initial speed.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def set_ball_site(self):
        """
        Function: set initial site.
        """
        self.ball.x = (self.window.width-self.ball.height)/2
        self.ball.y = (self.window.height-self.ball.height)/2

    def ball_move(self):
        """
        Function: the distance the ball moves each time.
        """
        self.ball.move(self.__dx, self.__dy)

    def get_ball_outside(self):
        """
        Function: Report when the ball outside.
        """
        if self.ball.y > self.window.height:
            return True

    def ball_rest(self):
        """
        Function: Set the initialization of the ball
        """
        self.set_ball_site()
        self.set_ball_velocity()
        while True:
            if self.star_switch:
                print(f'ball_rest {self.star_switch}')
                self.star_switch = False
                break
            pause(200)

    def ball_rebound_window(self):
        """
        Function: The ball bounces to the window.
        """
        if self.ball.x <= 0 or (self.ball.x + self.ball.width) >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def ball_rebound_obj(self):
        """
        Function: The ball bounces to the object.
        """
        obj_u = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y - 0.1)
        obj_d = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y + self.ball.height + 0.1)
        obj_l = self.window.get_object_at(self.ball.x - 0.1, self.ball.y + self.ball.height/2)
        obj_r = self.window.get_object_at(self.ball.x + self.ball.width + 0.1, self.ball.y + self.ball.height/2)

        if obj_u is not None:
            self.ball.y = obj_u.y + obj_u.height
            self.__dy = -self.__dy
            if obj_u != self.paddle:
                self.window.remove(obj_u)
                self.brick_number -= 1
        elif obj_d is not None:
            self.ball.y = obj_d.y - self.ball.height
            self.__dy = -self.__dy
            if obj_d != self.paddle:
                self.window.remove(obj_d)
                self.brick_number -= 1
        elif obj_l is not None:
            self.ball.x = obj_l.x + obj_l.width
            self.__dx = -self.__dx
            if obj_l != self.paddle:
                self.window.remove(obj_l)
                self.brick_number -= 1
        elif obj_r is not None:
            self.ball.x = obj_r.x - self.ball.width
            self.__dx = -self.__dx
            if obj_r != self.paddle:
                self.window.remove(obj_r)
                self.brick_number -= 1
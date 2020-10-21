"""
Graphics Class

Quote : Gobject、GWindow
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
BOUNDARY_X = 40
BOUNDARY_Y = 10

#-------------------------------------------------

FRAME_RATE = 100

BALL_SIZE = 20
BALL_Y_SPEED = 6
BALL_X_SPEED_MAX = 5

PADDLE_WIDTH = 100      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

LIVES = 99

class NoGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 boundary_x=BOUNDARY_X, boundary_y=BOUNDARY_Y):
        # 介面碼定義
        self.__menu_code = 0    # 介面碼 0:wait 1:main 2:game 9:none
        # 狀態碼定義
        self.__status_code = 0  # 狀態碼 0:wait 1:start 9:reade

        # 邊界定義
        self.__boundary_x = boundary_x
        self.__boundary_y = boundary_y

        # 建視窗
        self.window = GWindow(width=window_width, height=window_height, title='NONO', color="green")

        self.__obj = None

    def grid_line(self, size=50, dx=0, dy=0):
        """
        功能:輔助功能,方格線
        size = 單位方格大小
        dx = x軸位移量
        dy = y軸位移量
        """
        line_color = 'lightgray'

        # 水平輔助線
        for r in range(self.window.width // size + 1):
            p1_x = r * size + dx
            p1_y = 0  
            p2_x = r * size + dx
            p2_y = self.window.height

            line_row = GLine(p1_x, p1_y, p2_x, p2_y)
            line_row.color = line_color
            
            self.window.add(line_row)
        
        # 垂直輔助線
        for c in range(self.window.height // size + 1):
            p1_x = 0
            p1_y = c * size + dy
            p2_x = self.window.width
            p2_y = c * size + dy

            line_column = GLine(p1_x, p1_y, p2_x, p2_y)
            line_column.color = line_color
            
            self.window.add(line_column)


class NoMainmenu(NoGraphics):
    """docstring for NoMainmenu"""
    def __init__(self):
        super().__init__()

        #介面碼:1

        self.obj_txt = {}
        self.obj_rect = {}

        # TODO: 父類的私有變數無法傳到子類中
        print(self.__boundary_x)


    def start_main_menu(self):
        """功能:開啟主選單"""

        #建立邊界區

        #線
        self.__build_zone()
        #文字:標題
        self.__build_txt()
        #按鈕:啟動鈕

        self.__menu_code = 1    # 介面碼 0:wait 1:main 2:game 9:none
        self.__status_code = 0  # 狀態碼 0:wait 1:start 9:ready

        return True #開啟就緒

    def exit_main_menu(self):
        """功能:關閉主選單"""

        #判別條件: 處於main menu中

        # 使用pop逐一清掉:self.obj_txt
        while len(self.obj_txt) != 0:
            del_obj = self.obj_txt.popitem()
            self.window.remove(del_obj)

        # 使用pop逐一清掉:self.obj_rect
        while len(self.obj_rect) != 0:
            del_obj = self.obj_rect.popitem()
            self.window.remove(del_obj)

        self.__menu_code = 0    # 介面碼 0:wait 1:main 2:game 9:none
        self.__status_code = 0  # 狀態碼 0:wait 1:start 9:ready

        return True #關閉就緒
        
    def __build_txt(self, dx=0, dy=0):
        font = 'Times New Roman'


        # 開始 start_game
        start_game = GLabel('Start', x=200 + self.__boundary_x + dx, y=400 + self.__boundary_y + dy)
        start_game.font = f'{font}-50'
        start_game.color = "dimgray"
        self.window.add(start_game)
        self.obj_txt['start'] = start_game
        
        # 大標體 tital
        tital = GLabel('Breakout clone', x=200 + self.__boundary_x + dx, y=200 + self.__boundary_y + dy)
        tital.font = f'{font}-100'
        tital.color = "darkgray"
        self.window.add(tital)
        self.obj_txt['tital'] = tital

        # 中標題 subtitle
        subtitle = GLabel('Maker : Tsai NoNo', x=200 + self.__boundary_x + dx, y=300 + self.__boundary_y + dy)
        subtitle.font = f'{font}-50'
        subtitle.color = "gray"
        self.window.add(subtitle)
        self.obj_txt['subtitle'] = subtitle

        return 'self.obj_txt is ok'

    def __build_zone(self, dx=0, dy=0):

        zone_w = self.window.width - 2 * self.__boundary_x
        zone_h = self.window.height - 2 * self.__boundary_y

        main_zone = GRect(zone_w, zone_h, x=self.__boundary_x + dx, y=self.__boundary_y + dy)
        self.window.add(main_zone)
        self.obj_rect['main_zone'] = main_zone
        # self.obj_rect.append('zone')
        return 'self.obj_rect is ok'

    def mode_chack(self):
        pass


class NoMousePerform(NoGraphics):
    # 建立滑鼠執行腳本
    def __init__(self):
        super().__init__()

    
    def click_perform(self, mouse):
        pass

    def move_perform(self, mouse):
        # 判斷滑鼠指向的物件
        get_obj = self.window.get_object_at(mouse.x, mouse.y)

        # 主選單的移動方案 介面碼:1 
        if self.__menu_code == 1:
            if get_obj == self.obj_txt['start']:
                self.obj_txt['start'].color = "red"
            else:
                self.obj_txt['start'].color = "dimgray"

        # # 遊戲的移動方案 介面碼:2
        # elif self.__menu_code == 2:
        #     self.__game_paddle_move(mouse)
        #     if self.__status_code == 0:
        #         if get_obj == self.__obj_game_ball:
        #             self.__obj_game_ball.fill_color = "red"
        #     else:
        #         self.__obj_game_ball.fill_color = "black"

        # if get_obj == self.__obj_main_button:
        #     self.__obj_main_button.color = "dimgray"
        #     self.__obj_main_button.fill_color = "dimgray"
        # else:
        #     self.__obj_main_button.color = "red"
        #     self.__obj_main_button.fill_color = "red"
 




class NoBreakout(NoGraphics):

    def __init__(self, lives=LIVES, frame_rate=FRAME_RATE):
        super().__init__()
        self.__game_lives = lives
        self.__game_integral = 0
        self.__frame_rate = 1000 / frame_rate

        self.__obj_game_integral = None
        self.__obj_game_lives = None
        self.__obj_game_brick = None

        # Identify code
        self.__menu_code = 9    # 介面碼 0:main 1:game 9:none
        self.__status_code = 0  # 狀態碼 0:wait 1:start 9:reade
        self.__obj_menu_code = None
        self.__obj_status_code = None

        # main menu
        self.__obj_main_txt_1 = None
        self.__obj_main_txt_2 = None
        self.__obj_main_txt_start = None
        self.__obj_main_button = None
        self.__obj_main_zone = None

        # game menu
        self.__obj_game_zone_line_u = None
        self.__obj_game_zone_line_d = None
        self.__obj_game_zone_line_l = None
        self.__obj_game_zone_line_r = None
        self.brick = None

        self.__game_zone_u = 0
        self.__game_zone_d = 0
        self.__game_zone_l = 0
        self.__game_zone_r = 0

        self.__game_zone_w = 0
        self.__game_zone_h = 0

        # game brick
        self.__game_brick_num = 0

        # game ball
        self.__game_ball_size = BALL_SIZE
        self.__obj_game_ball = None

        self.__game_ball_vx = 0
        self.__game_ball_vy = 0

        self.__start_bool = False

        # game paddle
        self.__game_paddle_w = PADDLE_WIDTH
        self.__game_paddle_h = PADDLE_HEIGHT
        self.__game_paddle_offset = PADDLE_OFFSET
        self.__obj_game_paddle = None

        self.main_code_star()
        # self.main_button()  # 首頁返回鈕
        print(f'<<< end >>>')

    def main_code_star(self):
        # self.__obj_menu_code=GLabel(f'menu :{self.__menu_code}',x= self.__boundary_x + 1000, y=self.__boundary_y + 300)
        # self.__obj_menu_code.font = '-50'
        # self.window.add(self.__obj_menu_code)
        #
        # self.__obj_status_code=GLabel(f'status :{self.__status_code}',x= self.__boundary_x + 1000, y=self.__boundary_y + 400)
        # self.__obj_status_code.font = '-50'
        # self.window.add(self.__obj_status_code)

        self.__obj_game_lives = GLabel(f'lives = {self.__game_lives}',x= self.__boundary_x + 750, y=self.__boundary_y + 700)
        self.__obj_game_lives.font = '-25'
        self.window.add(self.__obj_game_lives)

        self.__obj_game_integral = GLabel(f'integral = {self.__game_integral}', x=self.__boundary_x + 0, y=self.__boundary_y + 700)
        self.__obj_game_integral.font = '-25'
        self.window.add(self.__obj_game_integral)

        # self.__obj_game_brick = GLabel(f'status :{self.__game_brick_num}', x=self.__boundary_x + 1000, y=self.__boundary_y + 200)
        # self.__obj_game_brick.font = '-50'
        # self.window.add(self.__obj_game_brick)

    def main_code_update(self):
        # self.__obj_menu_code.text = f'menu :{self.__menu_code}'
        # self.__obj_status_code.text = f'status :{self.__status_code}'
        self.__obj_game_lives.text = f'lives :{self.__game_lives}'
        self.__obj_game_integral.text = f'integral :{self.__game_integral}'
        # self.__obj_game_brick.text = f'brick :{self.__game_brick_num}'

    def mouse_start(self):
        onmousemoved(self.move_perform)
        onmouseclicked(self.click_perform)

    def main_menu(self, dx=0, dy=0):
        self.__menu_code = 0

        # 建立邊界區
        self.boundary_zone()

        # 大標體
        self.__obj_main_txt_1 = GLabel('Breakout clone', x=200 + self.__boundary_x + dx, y=200 + self.__boundary_y + dy)
        self.__obj_main_txt_1.font = f'Times New Roman-100'
        self.window.add(self.__obj_main_txt_1)

        # 中標題
        self.__obj_main_txt_2 = GLabel('Maker : Tsai NoNo', x=200 + self.__boundary_x + dx, y=300 + self.__boundary_y + dy)
        self.__obj_main_txt_2.font = f'Times New Roman-50'
        self.__obj_main_txt_2.color = "gray"
        self.window.add(self.__obj_main_txt_2)

        # 開始
        self.__obj_main_txt_start = GLabel('Start', x=200 + self.__boundary_x + dx, y=400 + self.__boundary_y + dy)
        self.__obj_main_txt_start.font = f'Times New Roman-50'
        self.__obj_main_txt_start.color = "dimgray"
        self.window.add(self.__obj_main_txt_start)
        self.main_code_update()

    def game_menu(self):
        self.__menu_code = 1
        self.boundary_zone()
        self.main_code_update()

    def menu_exit(self):
        """
        清除所有的物件
        1.地毯式:優點:程式短，無差別清除，缺點:較久，無法針對特定
        2.標記式:優點:快速，針對特定清除，缺點:每一筆都需記憶變數
        """

        for i in range(0, self.window.width-300, 20):
            for j in range(0, self.window.height, 25):
                get_obj = self.window.get_object_at(i, j)
                self.window.remove(get_obj)
        #
        self.window.remove(self.__obj_main_txt_1)
        self.window.remove(self.__obj_main_txt_2)
        self.window.remove(self.__obj_main_txt_start)
        self.window.remove(self.__obj_main_zone)
        #
        self.window.remove(self.__obj_game_zone_line_u)
        self.window.remove(self.__obj_game_zone_line_d)
        self.window.remove(self.__obj_game_zone_line_l)
        self.window.remove(self.__obj_game_zone_line_r)
        #
        self.window.remove(self.__obj_game_ball)
        self.window.remove(self.__obj_game_paddle)

    def main_button(self, dx=0, dy=0):
        self.__obj_main_button = GOval(50, 50, x=1100 + self.__boundary_x + dx, y=600 + self.__boundary_y + dy)
        self.__obj_main_button.color = 'red'
        self.__obj_main_button.filled = True
        self.__obj_main_button.fill_color = 'red'
        self.window.add(self.__obj_main_button)

    def boundary_zone(self, dx=0, dy=0):

        if self.__menu_code == 0:
            # Main Zone
            main_zone_w = self.window.width - 2 * self.__boundary_x
            main_zone_h = self.window.height - 2 * self.__boundary_y

            self.__obj_main_zone = GRect(main_zone_w, main_zone_h, x=self.__boundary_x + dx, y=self.__boundary_y + dy)
            self.window.add(self.__obj_main_zone)

        elif self.__menu_code == 1:
            # Game Zone
            self.__game_zone_w = self.window.width - 2 * self.__boundary_x - 300
            self.__game_zone_h = self.window.height - 2 * self.__boundary_y

            self.__game_zone_u = self.__boundary_y
            self.__game_zone_d = self.__boundary_y + self.__game_zone_h
            self.__game_zone_l = self.__boundary_x
            self.__game_zone_r = self.__boundary_x + self.__game_zone_w

            print(f'{self.__game_zone_w} , {self.__game_zone_h}')

            self.__obj_game_zone_line_u = GLine(self.__game_zone_l, self.__game_zone_u,
                                                self.__game_zone_r, self.__game_zone_u)
            self.__obj_game_zone_line_d = GLine(self.__game_zone_l, self.__game_zone_d,
                                                self.__game_zone_r, self.__game_zone_d)
            self.__obj_game_zone_line_l = GLine(self.__game_zone_l, self.__game_zone_u,
                                                self.__game_zone_l, self.__game_zone_d)
            self.__obj_game_zone_line_r = GLine(self.__game_zone_r, self.__game_zone_u,
                                                self.__game_zone_r, self.__game_zone_d)

            self.window.add(self.__obj_game_zone_line_u)
            self.window.add(self.__obj_game_zone_line_d)
            self.window.add(self.__obj_game_zone_line_l)
            self.window.add(self.__obj_game_zone_line_r)

    def click_perform(self, mouse):
        get_obj = self.window.get_object_at(mouse.x, mouse.y)

        # 進入遊戲畫面
        if get_obj == self.__obj_main_txt_start and self.__menu_code != 1 and self.__status_code == 0:
            self.__menu_code = 1    # feedback
            print("<<< up to game >>>")
            self.menu_exit()
            self.game_menu()
            self.game_brick_build(self.game_level_formation(level=1))
            self.game_ball_build()
            self.game_paddle_build()
            self.set_game_ball_rest()
            self.game_star()
        # 進入主畫面
        # elif get_obj == self.__obj_main_button and self.__menu_code != 0:
        #     self.__menu_code = 0    # feedback
        #     # self.__status_code == 0
        #     print(f'get_obj:self.__obj_main_button menu_code:{self.__menu_code} status_code:{self.__status_code}')
        #     print("<<< up to main >>>")
        #     self.menu_exit()
        #     self.main_menu()
        elif get_obj == self.__obj_game_ball and self.__menu_code == 1 and self.__status_code == 0:
            print(f'get_obj:self.__obj_game_ball menu_code:{self.__menu_code} status_code:{self.__status_code}')
            print(f'ok star')
            self.__start_bool = True
            self.main_code_update()
        elif get_obj is not None:
            print(f'obj')
            print(f'get_obj:??? menu_code:{self.__menu_code} status_code:{self.__status_code}')
        else:
            print(f'None')
        # print(str(get_obj))

    def move_perform(self, mouse):
        get_obj = self.window.get_object_at(mouse.x, mouse.y)

        if self.__menu_code == 0:
            if get_obj == self.__obj_main_txt_start:
                self.__obj_main_txt_start.color = "red"
            else:
                self.__obj_main_txt_start.color = "dimgray"

        # 針對遊戲畫面，做各狀態判斷
        elif self.__menu_code == 1:
            self.__game_paddle_move(mouse)
            if self.__status_code == 0:
                if get_obj == self.__obj_game_ball:
                    self.__obj_game_ball.fill_color = "red"
            else:
                self.__obj_game_ball.fill_color = "black"

        # if get_obj == self.__obj_main_button:
        #     self.__obj_main_button.color = "dimgray"
        #     self.__obj_main_button.fill_color = "dimgray"
        # else:
        #     self.__obj_main_button.color = "red"
        #     self.__obj_main_button.fill_color = "red"

    @staticmethod
    def game_level_formation(self, level=1):
        """
        0 一單位空
        1 一單位磚
        2 二單位磚
        3 三單位磚
        _ NONE

        :param level:
        :return:
        """
        if level == 1:
            formation = "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|" \
                        "1111111111|"

        return formation

    def game_brick_build(self, formation, b_w=85, b_h=20, b_offset_x=5, b_offset_y=30, b_spacing=5,
                         row_max=10, cow_max=10):
        j = 0
        num_cow = 0
        dy = self.__boundary_y + b_offset_y
        while formation.find('|') != -1:

            if num_cow == cow_max:
                break

            # 抓第一段字串
            site = formation[: formation.find('|')]
            # 存放剩下字串
            formation = formation[formation.find('|') + 1:]

            # 將字串轉換成磚塊
            dx = self.__boundary_x + b_offset_x/2
            num_row = 0
            for i in site:
                if i != '0' and i != '_':
                    num_row += int(i)
                    if num_row <= row_max:
                        self.brick = GRect(b_w * int(i) + b_spacing * (int(i)-1), b_h, x=dx, y=dy)
                        dx += (b_w + b_spacing) * int(i)
                        self.__game_brick_num += 1
                elif i == '0':
                    num_row += 1
                    dx += b_w + b_spacing

                self.brick.filled = True
                self.window.add(self.brick)
                self.game_brick_color(j)

            print(f'{site} {j} {num_row} {self.__game_brick_num}')

            dy += b_h + b_spacing
            j += 1
            num_cow += 1

    def game_brick_color(self, j, mode=1):
        if mode == 1:
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
        # 亂數給特殊磚-高分
        if random.randint(1, 10) == 1:
            self.brick.fill_color = 'red'

    def game_paddle_build(self):

        paddle_width = 75
        paddle_height = 15
        paddle_offset = 50
        # Create a paddle.
        print(f'paddle {self.__game_zone_w}  {self.__obj_game_ball.width}')
        self.__obj_game_paddle = GRect(self.__game_paddle_w, self.__game_paddle_h,
                                       x=(self.__game_zone_w - self.__game_paddle_w) /2 + self.__boundary_x,
                                       y=self.__game_zone_h - self.__game_paddle_offset + self.__boundary_y)
        print(f'paddle x={self.__obj_game_paddle.x}, y= {self.__obj_game_paddle.y}')

        self.__obj_game_paddle.filled = True
        self.window.add(self.__obj_game_paddle)

    def __game_paddle_move(self, mouse):
        if (mouse.x <= self.__game_zone_r - self.__game_paddle_w/2) and (mouse.x >= self.__game_zone_l + self.__game_paddle_w/2):
            self.__obj_game_paddle.x = mouse.x - (self.__game_paddle_w/2)
            # print(mouse.x)
        elif mouse.x < self.__game_zone_l:
            self.__obj_game_paddle.x = self.__game_zone_l
            # print(mouse.x)
        elif mouse.x > self.__game_zone_r:
            self.__obj_game_paddle.x = self.__game_zone_r - self.__game_paddle_w
            # print(mouse.x)

    def game_star(self):

        num_lives = self.__game_lives
        print(f'game_star : OK')
        while True:
            if self.__menu_code == 0:
                break
            if self.get_ball_outside():
                self.__game_lives -= 1
                self.main_code_update()
                if self.__game_lives > 0:
                    print('1')
                    self.__status_code = 0
                    self.set_game_ball_rest()
                    self.ball_speed_update()
                else:
                    print('1 end')
                    break
            if self.__game_brick_num == 0:
                print('2 end')
                break
            self.game_ball_move()
            self.ball_rebound_window()
            self.ball_rebound_obj()
            pause(self.__frame_rate)
        print('Game over')

    def game_ball_build(self):
        # Center a filled ball in the graphical window.
        self.__obj_game_ball = GOval(self.__game_ball_size, self.__game_ball_size,
                                    x=(self.__game_zone_w - self.__game_ball_size)/2 + self.__boundary_x,
                                    y=(self.__game_zone_h - self.__game_ball_size)/2 + self.__boundary_y)
        print(f'ball x={self.__obj_game_ball.x}, y={self.__obj_game_ball.y}')
        self.__obj_game_ball.filled = True
        self.window.add(self.__obj_game_ball)

        # self.__start_bool = True

    def __set_ball_velocity(self):
        self.__game_ball_vx = random.randint(1, BALL_X_SPEED_MAX)
        if random.random() > 0.5:
            self.__game_ball_vx = -self.__game_ball_vx
        self.__game_ball_vy = BALL_Y_SPEED
        print(f'set_ball_velocity {self.__game_ball_vx}, {self.__game_ball_vy}')

    def __set_ball_site(self):
        self.__obj_game_ball.x = (self.__game_zone_w - self.__game_ball_size) / 2 + self.__boundary_x
        self.__obj_game_ball.y = (self.__game_zone_h - self.__game_ball_size) / 2 + self.__boundary_y

    def game_ball_move(self):
        print(f'ball_move {self.__game_ball_vx}, {self.__game_ball_vy}')
        self.__obj_game_ball.move(self.__game_ball_vx, self.__game_ball_vy)

    def get_ball_outside(self):
        if self.__obj_game_ball.y > self.window.height-self.__boundary_y - self.__game_ball_size:
            return True

    def get_brick_number(self):
        return self.__game_brick_num

    def set_game_ball_rest(self):
        print(f'ball_rest : start')
        self.__set_ball_site()
        self.__set_ball_velocity()
        while True:
            if self.__start_bool:
                print(f'ball_rest {self.__start_bool}')
                self.__start_bool = False
                break
            pause(200)
        print(f'ball_rest : end')
        self.__status_code = 1

    def ball_rebound_window(self):
        if self.__obj_game_ball.x <= self.__game_zone_l or \
                (self.__obj_game_ball.x + self.__obj_game_ball.width) >= self.__game_zone_r:
            print('撞到兩側')
            self.__game_ball_vx = -self.__game_ball_vx

        if self.__obj_game_ball.y <= self.__game_zone_u:
            print('撞到上面')
            self.__game_ball_vy = -self.__game_ball_vy

            #下邊界要拿掉的
        if self.__obj_game_ball.y >= self.__game_zone_d - self.__obj_game_ball.height:
            print('撞到下面')
        #     self.__game_ball_vy = -self.__game_ball_vy

    def ball_rebound_obj(self):
        non_remove_obj = []
        non_remove_obj.append(self.__obj_game_paddle)
        non_remove_obj.append(self.__obj_game_zone_line_u)
        non_remove_obj.append(self.__obj_game_zone_line_d)
        non_remove_obj.append(self.__obj_game_zone_line_l)
        non_remove_obj.append(self.__obj_game_zone_line_r)

        non_rebound_obj = []
        non_rebound_obj.append(self.__obj_game_lives)
        non_rebound_obj.append(self.__obj_game_integral)

        ball_touch_obj = []
        ball_touch_obj.append(self.window.get_object_at
                              (self.__obj_game_ball.x + self.__obj_game_ball.width / 2,
                               self.__obj_game_ball.y - 0.1))
        ball_touch_obj.append(self.window.get_object_at
                              (self.__obj_game_ball.x + self.__obj_game_ball.width / 2,
                               self.__obj_game_ball.y + self.__obj_game_ball.height + 0.1))
        ball_touch_obj.append(self.window.get_object_at
                              (self.__obj_game_ball.x - 0.1,
                               self.__obj_game_ball.y + self.__obj_game_ball.height / 2))
        ball_touch_obj.append(self.window.get_object_at
                              (self.__obj_game_ball.x + self.__obj_game_ball.width + 0.1,
                               self.__obj_game_ball.y + self.__obj_game_ball.height / 2))

        j = 0
        for i in ball_touch_obj:
            if i is not None:
                if i not in non_rebound_obj:
                    if i not in non_remove_obj:
                        if i.fill_color == 'red':
                            self.__game_integral += 50
                        else:
                            self.__game_integral += 10
                        self.window.remove(i)
                        self.__game_brick_num -= 1
                        self.main_code_update()

                    if j == 0:
                        if i == self.__obj_game_paddle:
                            self.__obj_game_ball.y = self.__obj_game_paddle.y + self.__game_paddle_h
                        self.__game_ball_vy = -self.__game_ball_vy
                    elif j == 1:
                        if i == self.__obj_game_paddle:
                            self.__obj_game_ball.y = self.__obj_game_paddle.y - self.__obj_game_ball.height
                        self.__game_ball_vy = -self.__game_ball_vy
                    elif j == 2:
                        if i == self.__obj_game_paddle:
                            self.__obj_game_ball.x = self.__obj_game_paddle.x + self.__game_paddle_w
                        self.__game_ball_vx = -self.__game_ball_vx
                    # print(f'obj_r')
                    elif j == 3:
                        if i == self.__obj_game_paddle:
                            self.__obj_game_ball.x = self.__obj_game_paddle.x - self.__obj_game_ball.width
                        self.__game_ball_vx = -self.__game_ball_vx
            j += 1

    def ball_speed_update(self, threshold=100):
        speed = 10
        if self.__game_integral % threshold == 0 and self.__game_integral != 0:
            self.__frame_rate = 1000 / (FRAME_RATE + speed)

    
"""
Breakout clone

maker: Tasi nono
"""

from nographics import NoGraphics, NoMainmenu, NoMousePerform

NUM_LIVES = 3


def main():
    main_menu = NoMainmenu()

    main_menu.start_main_menu()

    main_menu.exit_main_menu()

    #開啟滑鼠功能
    NoMousePerform()

if __name__ == '__main__':
    main()
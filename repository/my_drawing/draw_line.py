"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE=10
window = GWindow()
start_point = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    Function:   record the first point, and draw a line when the second point,
                cancel the circle at the first point
    Principle:  Use global variables to record the first point,
                and each click determines whether there is a record of the first point
    :param mouse: mouse Information
    """
    global start_point

    if start_point is None:
        start_point = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(start_point)

    else:
        second_line = GLine(start_point.x, start_point.y, mouse.x, mouse.y)
        window.remove(start_point)
        start_point = None
        window.add(second_line)


if __name__ == "__main__":
    main()

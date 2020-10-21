"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""
import math
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GPolygon
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	:return:
	"""
	if order == 0:
		return
	else:
		# 運算出倒三角的三點位置
		point_list = three_point(length / 2)

		# 依序對三點位置，做下一階的遞迴運算
		for point in point_list:
			sierpinski_triangle(order - 1, length / 2, upper_left_x + point[0], upper_left_y + point[1])

		# 只印最後的 1 order，減少重複顯示
		if order == 1:
			draw_triangle(length, upper_left_x, upper_left_y)
			# pause(400)


def three_point(length):
	"""
	功能:描繪三點(x,y)位置，運用極座標-三角函數與長度
	:param length: 長度
	:return point_list(list): 內有三點各自的(x,y)位置
	"""
	point_list = []
	# 初始化
	dis_x = 0
	dis_y = 0

	# 運用三角函數，描繪三點位置
	for edge in range(3):
		# 從角度轉成弧
		rad = math.radians(-120 * edge)
		# x向右為正，(+)cos
		dis_x += length * math.cos(rad)
		# y向下為正，(-)sin
		dis_y += -length * math.sin(rad)

		point_list.append((dis_x, dis_y))

	return point_list


def draw_triangle(length, start_x, start_y):
	"""
	功能:
	:param length:
	:param start_x:
	:param start_y:
	:return:
	"""
	triangle = GPolygon()
	triangle.add_vertex((start_x, start_y))
	for edge in range(3):
		triangle.add_polar_edge(length, -120 * edge)
	window.add(triangle)


if __name__ == '__main__':
	main()
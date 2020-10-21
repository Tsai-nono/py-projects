"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
SIZE = 2


def main():
	"""
	Function: Build a rocket
	Principle: SIZE determines the size (excluding 0), the rocket is divided into head, belt, upper, lower, belt, head
	"""

	if SIZE == 0:
		print('not zero')
	else:
		rocket_head(SIZE)
		rocket_belt(SIZE)
		rocket_upper(SIZE)
		rocket_lower(SIZE)
		rocket_belt(SIZE)
		rocket_head(SIZE)


def rocket_head(size):
	'''
	Function: build rocket head
	:param size: int,The number of layers of the rocket
	'''

	for i in range(size):
		for j in range(size+1):
			if j < (size-i):
				print(' ', end='')
			else:
				print('/', end='')

		for j in range(size+1):
			if j > i:
				print(' ', end='')
			else:
				print('\\', end='')
		print('')


def rocket_belt(size):
	'''
	Function: build rocket belt
	:param size: int,The number of layers of the rocket
	'''

	rocket_width = 2 * (size+1)
	for i in range(rocket_width):
		if i == 0:
			print('+', end='')
		elif i == (rocket_width-1):
			print('+', end='')
		else:
			print('=', end='')
	print('')


def rocket_upper(size):
	'''
	Function: build rocket upper
	:param size: int,The number of layers of the rocket
	'''

	for i in range(size):
		for j in range(size+1):

			if j == 0:
				print('|', end='')
			elif j < (size-i):
				print('.', end='')
			else:
				if (i + j + (size % 2)) % 2 == 0:
					print('/', end='')
				else:
					print('\\', end='')

		for j in range(size+1):
			if j == size:
				print('|', end='')
			elif j > i:
				print('.', end='')
			else:
				if (size - i + j + (size % 2)) % 2 == 0:
					print('\\', end='')
				else:
					print('/', end='')
		print('')


def rocket_lower(size):
	'''
	Function: build rocket lower
	:param size: int,The number of layers of the rocket
	'''

	for i in range(size):
		for j in range(size+1):
			if j == 0:
				print('|', end='')
			elif j <= i:
				print('.', end='')
			else:
				if (size - i + j + (size % 2)) % 2 == 0:
					print('/', end='')
				else:
					print('\\', end='')

		for j in range(size+1):

			if j == size:
				print('|', end='')
			elif j >= (size-i):
				print('.', end='')
			else:
				if (i + j + (size % 2)) % 2 == 0:
					print('\\', end='')
				else:
					print('/', end='')
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
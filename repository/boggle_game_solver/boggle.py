"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""
from boggle_logging import Logging
from boggle_dictionary import Dictionary_Dict

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
DICT_FILE = 'dictionary.txt'
LOG_FILE = 'boggle_4x4_1.txt'

SIZE = 4


def main():
	"""
	TODO:
	"""
	# 跑分版本
	tester()

	# 正式版本
	# formal()


def formal():
	# Build: Dictionary (obj)
	diction = set_dictionary(DICT_FILE)

	# Build: effective_list (list)
	effective_list = set_effective_list(SIZE, SIZE)

	# Build: boggle_list (list)
	boggle_list = []
	input_row = 0
	while True:
		if input_row == 4:
			break
		else:
			txt = input(f'{input_row+1} row of letters: ').split()

			if len(txt) == SIZE:
				if False not in [False for x in txt if len(x) != 1]:
					boggle_list.append(txt)
					input_row += 1
				else:
					print('not two word')
			else:
				print('again')

	# Execution: permutation and query
	ans_list = []
	for i in range(1, SIZE + 1):
		for j in range(1, SIZE + 1):
			permutation(i, j, '', ans_list, effective_list, boggle_list, diction)
	print(f'There are {len(ans_list)} words in total.')


def tester():
	# Build: Logging (obj)
	logging = set_logging(LOG_FILE)
	# Build: Dictionary (obj)
	diction = set_dictionary(DICT_FILE)

	# Log: setting time input log
	logging.write_log(['\n','>>>>>>>\n','star boggle.py\n','setting end\n'])

	# Build: boggle_list (list)
	boggle_list = logging.boggle_list

	column = logging.column
	row = logging.row

	# Build: effective_list (list)
	effective_list = set_effective_list(column,row)


	for i in range(3):
		logging.reset_time()
		
		print(f'>>Perform the {i+1} test<<')
		
		ans_list = []
		for i in range(1, column + 1):
			for j in range(1, row + 1):
				permutation(i, j, '', ans_list, effective_list, boggle_list,diction)

		# Log: result input log
		logging.write_log(['\n',str(len(ans_list)),'\n',str(ans_list),'\n'])

	print(f'>>>>>Test End<<<<<')		


def permutation(x, y, ans_str, ans_list, effective_list, boggle_list,diction):

	if is_effective(x, y, effective_list) is False:
		return ans_list
	else:
		# setting
		effective_list[x][y] = 0
		ans_str = ans_str + boggle_list[x-1][y-1]

		# Enter the next path combination of eight directions
		for i in (x-1, x, x+1):
			for j in (y-1, y, y+1):
				if i == x and j == y:
					pass
				else:
					if effective_list[i][j] == 1 and has_prefix(ans_str,diction):
						permutation(i, j, ans_str, ans_list, effective_list, boggle_list, diction)

		# Dictionary query with more than 4 characters (ans_str)
		# Those who match are added to the answer list (ans_list)
		fit_answer(ans_str, ans_list, diction)

		# resetting
		ans_str = ans_str[:-1]
		effective_list[x][y] = 1


def fit_answer(ans_str,ans_list,diction):
	"""
	Function: Those who match are added to the answer list (ans_list)
			Dictionary query with more than 4 characters (ans_str)
	:param ans_str: (str) Combined answer string
	:param ans_list: (list) Answer list
	:param diction: (obj) Query dictionary object
	"""

	if len(ans_str) >= 4:
		if has_word(ans_str, diction) and ans_str not in ans_list:
			print(f'Found "{ans_str}"')
			ans_list.append(ans_str)


def is_effective(x, y, eff_list):
	"""
	Function: Is there a valid path at the location.
	:param x: (int) x coordinate
	:param y: (int) y coordinate
	:param eff_list: (list) effective_list
	:return: (bool) Is there a valid path
	"""
	
	for check_x in (x-1, x, x+1):
		for check_y in (y-1, y, y+1):
			if check_x == x and check_y == y:
				pass
			else:
				if eff_list[check_x][check_y] == 1:
					return True
	return False


def set_effective_list(column, row):
	"""
	Function: Create an effective matrix and use (0: invalid 1: valid) to record the path that can be taken.
	:param column: (int) x direction 
	:param row: (int) y direction 
	:return: (list) List of valid paths
	"""
	effective_list = [[0 for i in range(column + 2)] for j in range(row + 2)]

	for i in range(1, column + 1):
		for j in range(1, row + 1):
			effective_list[i][j] = 1
	return effective_list


def set_logging(file):
	"""
	Function: read the file add it to the Python list.
	:return: (obj) Objects with logging-related functions
	"""
	# Call: Logging Program
	logging = Logging(file)
	# Read: boggle import boggle_list
	logging.read_list()
	return logging


def set_dictionary(file):
	"""
	Function: read the file add it to the Python dict.
	:return: (obj) Objects with dictionary-related functions
	"""
	# Call: Dictionary Program
	diction = Dictionary_Dict(file)
	# Read: dictionary import dict_map
	diction.diction_dict()
	return diction


def has_word(sub_s, diction):
	"""
	Function: Query the dictionary for this word.
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param diction: (obj) Query dictionary object
	:return: (bool) If there is any words in sub_s
	"""
	if diction.lookup_dict_diciton(sub_s) == 2:
		return True
	else:
		return False


def has_prefix(sub_s, diction):
	"""
	Function: Query the dictionary for words with this prefix.
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param diction: (obj) Query dictionary object
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if diction.lookup_dict_diciton(sub_s) <= 2:
		return True
	else:
		return False


if __name__ == '__main__':
	main()

"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int,待判別整數
	:return: int,回傳n中最大之 unit 整數
	"""
	return find_largest_digit_helper(n)


def find_largest_digit_helper(n, max_n=0):
	"""
	:param n: int,待判別整數
	:param max_n: int,當下最大整數值
	:return: int,回傳n中最大之 unit 整數
	"""
	# 特殊情況:已達最大值9，就不需再比了
	if n == 0 or max_n == 9:
		return max_n
	else:
		# 負值轉換為正值
		if n < 0:
			n *= -1

		# 用餘數提出尾數
		unit_n = n % 10

		# 尾數比現在最大值
		if unit_n > max_n:
			max_n = unit_n

		# 因變數會隨 Recursive 結束而釋出，所以需將 function 放在回傳上
		return find_largest_digit_helper(n//10, max_n)


if __name__ == '__main__':
	main()

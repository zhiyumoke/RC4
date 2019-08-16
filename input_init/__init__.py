import numpy as np


def str_con():
	input_str = input("请输入密钥：")
	output_bit = []
	for cha in input_str:
		output_bit.append(ord(cha))
	output_bit = np.array(output_bit)
	return len(output_bit), output_bit


def key_stream(num):
	output_bit = list('{:08b}'.format(num))
	for i in range(8):
		if output_bit[i] == '0':
			output_bit[i] = 0
		elif output_bit[i] == '1':
			output_bit[i] = 1
	return output_bit


def two2chr(child_list=[]):
	if (child_list == np.array([0, 0, 0, 0])).all(): print('0', end='')
	if (child_list == np.array([0, 0, 0, 1])).all(): print('1', end='')
	if (child_list == np.array([0, 0, 1, 0])).all(): print('2', end='')
	if (child_list == np.array([0, 0, 1, 1])).all(): print('3', end='')
	if (child_list == np.array([0, 1, 0, 0])).all(): print('4', end='')
	if (child_list == np.array([0, 1, 0, 1])).all(): print('5', end='')
	if (child_list == np.array([0, 1, 1, 0])).all(): print('6', end='')
	if (child_list == np.array([0, 1, 1, 1])).all(): print('7', end='')
	if (child_list == np.array([1, 0, 0, 0])).all(): print('8', end='')
	if (child_list == np.array([1, 0, 0, 1])).all(): print('9', end='')
	if (child_list == np.array([1, 0, 1, 0])).all(): print('A', end='')
	if (child_list == np.array([1, 0, 1, 1])).all(): print('B', end='')
	if (child_list == np.array([1, 1, 0, 0])).all(): print('C', end='')
	if (child_list == np.array([1, 1, 0, 1])).all(): print('D', end='')
	if (child_list == np.array([1, 1, 1, 0])).all(): print('E', end='')
	if (child_list == np.array([1, 1, 1, 1])).all(): print('F', end='')

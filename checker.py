from utils import *

class InputChecker():

	def checker(input_char, calc_input):
		if is_operator(input_char) == True and is_plusminus(input_char) == False:
			return InputChecker.check_operator(input_char, calc_input)
		if input_char == '(':
			return InputChecker.open_bracket(calc_input)
		if input_char == ')':
			return InputChecker.close_bracket(calc_input)
		if input_char == '.':
			return InputChecker.check_dot(calc_input)
		return True
	
	def check_operator(input_char, calc_input):
		if calc_input == "":
			return False
		if calc_input[-1].isdigit() == True or calc_input[-1] == ')':
			return True
		return False

	def open_bracket(calc_input):
		if calc_input == "":
			return True
		if is_operator(calc_input[-1]) or calc_input[-1] == '(':
			return True
		return False

	def close_bracket(calc_input):
		if calc_input == "":
			return False
		if is_operator(calc_input[-1]) or calc_input[-1] == '(':
			return False
		x = bracket_cmp(calc_input)
		if x > 0:
			return True
		return False

	def check_dot(calc_input):
		rev = calc_input[::-1]
		for i in rev:
			if i == '.':
				return False
			if i.isdigit() == False:
				return True
		return True 	
	#Add functions that check valid use of operands and operators

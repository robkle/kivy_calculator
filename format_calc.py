from utils import *

class InputFormat():
	def all(calc_input):
		calc_input = InputFormat.dot('', calc_input)
		calc_input = InputFormat.brackets(calc_input)
		calc_input = InputFormat.operator(calc_input)
		return calc_input

	def dot(input_char, calc_input):
		if input_char == '.' and (calc_input == "" or calc_input == "Error"):
			calc_input = "0"
		elif calc_input != "" and calc_input != "Error":
			if calc_input[-1] == '.' and input_char.isdigit() == False:
				calc_input = calc_input[:-1]
			elif input_char == '.' and calc_input[-1].isdigit() == False:
				calc_input += "0"
		return calc_input

	def brackets(calc_input):
		x = bracket_cmp(calc_input)
		if x > 0:
			while x > 0:
				calc_input += ")"
				x -= 1
		return calc_input

	def operator(calc_input):
		if is_operator(calc_input[-1]) == True:
			return calc_input[:-1]
		return calc_input

from utils import *

class InputFormat():
	def dot(input_char, calc_input):
		if input_char == '.' and (calc_input == "" or calc_input == "Error"):
			calc_input = "0"
		elif calc_input != "" and calc_input != "Error":
			if calc_input[-1] == '.' and input_char.isdigit() == False:
				calc_input += "0"
			elif input_char == '.' and calc_input[-1].isdigit() == False:
				calc_input += "0"
		return calc_input

class InputChecker():
	def checker(input_char, calc_input):
		return True
		#if is_operator(input_char):
		#	return check_operator(input_char, calc_input)
	
	def check_operator(input_char, calc_input):
		pass
	#Add functions that check valid use of operands and operators

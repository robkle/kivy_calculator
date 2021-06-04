import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from checker import *

Window.size = (500 , 700)

Builder.load_file('calc.kv')

class CalcLayout(GridLayout):
	def backspace(self, calc_input):
		if calc_input == "Error":
			self.display.text = ""
		else:
			self.display.text = calc_input[:-1]
	def checker(self, input_char, calc_input):
		calc_input = InputFormat.dot(input_char, calc_input)
		if InputChecker.checker(input_char, calc_input):
			self.display.text = calc_input + input_char
	def calculate(self, calc_input):
		try:
			self.display.text = str(eval(calc_input))
		except Exception:
			self.display.text = "Error"


class CalculatorApp(App):
	def build(self):
		return CalcLayout()

if __name__ == "__main__":
	CalculatorApp().run()

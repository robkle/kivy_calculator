OPERATORS = "+-*/"
PLUSMINUS = "+-"

def is_operator(char):
	if char in OPERATORS:
		return True
	return False

def is_plusminus (char):
	if char in PLUSMINUS:
		return True
	return False

def bracket_cmp (string):
	open_count = 0
	close_count = 0
	for i in string:
		if i == '(':
			open_count += 1
		if i == ')':
			close_count += 1
	x = open_count - close_count
	return x

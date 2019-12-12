def get_command(prompt):
	command = input(prompt)
	
	return command

def dye(text):
	red = "\033[31m"
	deafultColor = "\033[m"
	return red + text + deafultColor

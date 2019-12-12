import os


class Command(object):
	red = "\033[31m"
	deafultColor = "\033[m"

	def __init__(self, execution_command):
		self.cmd = execution_command
		self.dir = os.getcwd()
	
	def exec(self):
		raise NotImplementedError
	
	def dye(self, text):
		return self.red + text + self.deafultColor
	
	def __str__(self):
		return self.cmd
	
	def __repr__(self):
		return f"Command {self.cmd} executed at {self.dir}"

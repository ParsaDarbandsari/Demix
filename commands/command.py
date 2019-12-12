import os


class Command(object):
	def __init__(self, execution_command):
		self.cmd = execution_command
		self.dir = os.getcwd()
	
	def exec(self):
		raise NotImplementedError
	
	
	def __str__(self):
		return self.cmd
	
	def __repr__(self):
		return f"Command {self.cmd} executed at {self.dir}"

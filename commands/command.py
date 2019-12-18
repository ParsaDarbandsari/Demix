import os


class Command(object):
	cmd = ''
	def __init__(self):
		self.dir = os.getcwd()
	
	def exec(self):
		raise NotImplementedError()
	
	
	def __str__(self):
		return self.cmd
	
	def __repr__(self):
		return f"Command '{self.cmd}' executed at: {self.dir}"

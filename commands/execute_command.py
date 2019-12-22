from commands.command import Command
from utils.utils import *
import os


class ExecuteCommand(Command):
	cmd = 'exc'
	usage = {
		'usage': f'{cmd} [file name]',
		'description': 'Runs an application or opens a file or a folder in File explorer'
	}
	def __init__(self, executing_file):
		super(ExecuteCommand, self).__init__()
		if executing_file != "":
			self.executing_file = executing_file
			self.exec()
		else:
			print(dye(f"usage: {self.usage['usage']}"))
		
	
	def exec(self):
		try:
			os.startfile(os.path.join(self.dir, self.executing_file))
		except FileNotFoundError:
			print(dye(f"FileNotFoundError: File '{self.executing_file}' does not exist"))
		except PermissionError:
			print(dye("PermissionError: Access Denied"))

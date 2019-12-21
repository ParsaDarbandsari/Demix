from commands.command import Command
from utils import utils
import os


class ExecuteCommand(Command):
	cmd = 'exc'
	usage = {
		'usage': f'{cmd} [file name]',
		'description': 'Runs an application or opens a file or a folder in File explorer'
	}
	def __init__(self, executing_file):
		super(ExecuteCommand, self).__init__()
		self.executing_file = executing_file
	
	def exec(self):
		try:
			os.startfile(os.path.join(self.dir, self.executing_file))
		except FileNotFoundError:
			print(utils.dye(f"FileNotFoundError: File '{self.executing_file}' does not exist"))
		except PermissionError:
			print(utils.dye("PermissionError: Access Denied"))

from commands.command import Command
from utils.utils import *
import os


class GoToDirectoryCommand(Command):
	cmd = "goto"
	usage = {
		'usage': f'{cmd} [directory_name]',
		'description': 'Switches to one of the subdirectories of your current directory (if any)'
	}
	
	def __init__(self, folder):
		super(GoToDirectoryCommand, self).__init__()
		self.folder = folder.replace('..', ' ')
	
	def exec(self):
		try:
			os.chdir(f"{self.dir}\\{self.folder}")
		except FileNotFoundError:
			print(dye(f"FileNotFoundError: Folder '{self.folder}' does not exist"))
		except PermissionError:
			print(dye(f"PermissionError: Access Denied"))

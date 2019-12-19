from commands.command import Command
from utils.utils import *
import os


class GoToDirectoryCommand(Command):
	cmd = "goto"
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

from commands.command import Command
from utils.utils import *
import os


class GoToDirectoryCommand(Command):
	cmd = "goto"
	def __init__(self, folder):
		self.folder = folder
		super(GoToDirectoryCommand, self).__init__()
	
	def exec(self):
		try:
			os.chdir(f"{self.dir}\\{self.folder}")
		except FileNotFoundError:
			print(dye(f"FileNotFoundError: Folder '{self.folder}' does not exist"))
		except PermissionError:
			print(dye(f"PermissionError: Access Denied"))

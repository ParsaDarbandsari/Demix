from commands.command import Command
from utils.utils import *
import os


class GoToDirectoryCommand(Command):
	def __init__(self, dir, folder):
		self.directory = dir
		self.folder = folder
		super(GoToDirectoryCommand, self).__init__("goto")
	
	def exec(self):
		try:
			os.chdir(f"{self.directory}\\{self.folder}")
		except FileNotFoundError:
			print(dye(f"FileNotFoundError: Folder '{self.folder}' does not exist"))
		except PermissionError:
			print(dye(f"PermissionError: You Do not have the access to go into the folder {self.folder}"))
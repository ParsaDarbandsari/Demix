from commands.command import Command
from utils.utils import *
import os


class GoToDirectoryCommand(Command):
	def __init__(self, folder):
		self.folder = folder
		super(GoToDirectoryCommand, self).__init__("goto")
	
	def exec(self):
		try:
			os.chdir(f"{self.dir}\\{self.folder}")
		except FileNotFoundError:
			print(dye(f"FileNotFoundError: Folder '{self.folder}' does not exist"))

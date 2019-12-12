from command.command import Command
import os


class GoToDirectoryCommand(Command):
	def __init__(self, folder):
		self.folder = folder
		super(GoToDirectoryCommand, self).__init__("goto")
	
	def exec(self):
		try:
			os.chdir(f"{os.getcwd()}\\{self.folder}")
		except FileNotFoundError:
			print(self.dye(f"FileNotFoundError: Folder '{self.folder}' does not exist"))
		except PermissionError:
			print(self.dye(f"PermissionError: You Do not have the access to go into the folder {self.folder}"))


class GoToParentDirectoryCommand(Command):
	def __init__(self):
		super(GoToParentDirectoryCommand, self).__init__("goback")
	
	def exec(self):
		parent_directory = os.getcwd()
		done = False
		letter_index = -1
		
		while not done:
			letter = parent_directory[letter_index]
			parent_directory = parent_directory[:-1]
			
			if letter == "\\":
				done = True
		
		os.chdir(parent_directory)
	
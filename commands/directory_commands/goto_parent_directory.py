from commands.command import Command
import os

class GoToParentDirectoryCommand(Command):
	def __init__(self, dir):
		super(GoToParentDirectoryCommand, self).__init__("goback")
		self.directory = dir
	
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

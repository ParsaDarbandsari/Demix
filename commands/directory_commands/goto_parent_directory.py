from commands.command import Command
import os

class GoToParentDirectoryCommand(Command):
	def __init__(self):
		super(GoToParentDirectoryCommand, self).__init__("goback")
	
	def exec(self):
		parent_directory = os.path.pardir
		os.chdir(parent_directory)

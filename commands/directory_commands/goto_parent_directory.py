from commands.command import Command
import os

class GoToParentDirectoryCommand(Command):
	cmd = 'goback'
	usage = {
		'usage': f'{cmd} (no extra info needed)',
		'description': 'Returns to the parent directory of the current directory'
	}
	
	def __init__(self):
		super(GoToParentDirectoryCommand, self).__init__()
	
	def exec(self):
		parent_directory = os.path.pardir
		os.chdir(parent_directory)

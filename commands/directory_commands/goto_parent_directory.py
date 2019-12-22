from commands.command import Command
from utils.utils import *
import os

class GoToParentDirectoryCommand(Command):
	cmd = 'goback'
	usage = {
		'usage': f'{cmd} (no extra info needed)',
		'description': 'Returns to the parent directory of the current directory'
	}
	
	def __init__(self, show_usage=False):
		super(GoToParentDirectoryCommand, self).__init__()
		if show_usage == True:
			print(dye(f"usage: {self.usage['usage']}"))
		else:
			self.exec()
	
	def exec(self):
		parent_directory = os.path.pardir
		os.chdir(parent_directory)

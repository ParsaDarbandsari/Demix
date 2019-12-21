from commands.command import Command
from utils import utils
import os

class NewDirectoryCommand(Command):
	cmd = 'nwdir'
	usage = {
		'usage': f'{cmd} [new directory name]',
		'description': 'Creates a new empty directory'
	}
	
	def __init__(self, new_directory_name):
		super(NewDirectoryCommand, self).__init__()
		self.new_directory_name = new_directory_name
	
	def exec(self):
		try:
			os.mkdir(os.path.join(self.dir, self.new_directory_name))
			print(f"Folder '{self.new_directory_name}' successfully created")
		except FileExistsError:
			print(utils.dye(f"FileExistsError: Directory '{self.new_directory_name}' already exists"))
		except PermissionError:
			print(utils.dye(f"PermissionError: Access Denied"))

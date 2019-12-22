from commands.command import Command
from utils.utils import *
import os

class NewDirectoryCommand(Command):
	cmd = 'nwdir'
	usage = {
		'usage': f'{cmd} [new directory name]',
		'description': 'Creates a new empty directory'
	}
	
	def __init__(self, new_directory_name):
		super(NewDirectoryCommand, self).__init__()
		if new_directory_name != "":
			self.new_directory_name = new_directory_name
			self.exec()
		else:
			print(dye(f"usage: {self.usage['usage']}"))
	
	def exec(self):
		try:
			os.mkdir(os.path.join(self.dir, self.new_directory_name))
			print(f"Folder '{self.new_directory_name}' successfully created")
		except FileExistsError:
			print(dye(f"FileExistsError: Directory '{self.new_directory_name}' already exists"))
		except PermissionError:
			print(dye(f"PermissionError: Access Denied"))

from commands.command import Command
from utils import utils
import shutil as shut
import os


class RemoveDirectoryCommand(Command):
	cmd = 'rmvdir'
	usage = {
		'usage': f'{cmd} [removing directory name]',
		'description': 'Removes an existing directory (whether empty or not)'
	}
	
	def __init__(self, directory_name):
		super(RemoveDirectoryCommand, self).__init__()
		self.removing_directory_name = directory_name
	
	def exec(self):
		try:
			os.rmdir(os.path.join(self.dir, self.removing_directory_name))
			print(f"Folder '{self.removing_directory_name}' successfully deleted")
		except FileNotFoundError:
			print(utils.dye(F"FileNotFoundError: Directory '{self.removing_directory_name}' does not exist"))
		except PermissionError:
			print(utils.dye(f"PermissionError: Access Denied"))
		except OSError:
			print(f"Folder {self.removing_directory_name} may contain some files,\n")
			delete = input(f"Are you sure you want to delete it? [Y/n]\n"
						   f"NOTE: There is No going back once the folder and it's files had been removed\n")
			delete = delete.upper()
			
			if delete == 'Y':
				shut.rmtree(os.path.join(self.dir, self.removing_directory_name))
				print("Deletion successful")
			else:
				print("Deletion canceled")

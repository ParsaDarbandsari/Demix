from commands.directory_commands.goto_parent_directory import GoToParentDirectoryCommand
from commands.directory_commands.goto_directory import GoToDirectoryCommand
from commands.directory_commands.remove_directory import RemoveDirectoryCommand
from commands.directory_commands.new_directory import NewDirectoryCommand
from commands.execute_command import ExecuteCommand
from utils.utils import *
import os

USERNAME = os.getenv('USERNAME')
user_home_directory = os.path.expanduser(os.getenv('USERPROFILE'))
demix_default_directory_name = "Demix"
demix_default_directory_path = f"{user_home_directory}\\{demix_default_directory_name}"
current_directory = user_home_directory
__author__ = 'Parsa Darbandsari <parsa.darbandsari@outlook.com>'
__version__ = '1.0'
PC_NAME = os.getenv('COMPUTERNAME')

NEW_DIRECTORY_COMMAND = "nwdir"  # done
REMOVE_DIRECTORY_COMMAND = "rmvdir"  # done
EXECUTE_COMMAND = "exc"
GO_TO_DIRECTORY_COMMAND = "goto"  # done
GO_TO_PARENT_DIRECTORY_COMMAND = "goback"  # done
LIST_COMMAND = "list"
EXIT_COMMAND = 'exit'
CLEARSCREEN_COMMAND = 'cls'
DEMIX_INFO_COMMAND = "-cmd"
COMMAND_LIST = [CLEARSCREEN_COMMAND, EXIT_COMMAND, LIST_COMMAND, GO_TO_PARENT_DIRECTORY_COMMAND,
				GO_TO_DIRECTORY_COMMAND, EXECUTE_COMMAND,
				REMOVE_DIRECTORY_COMMAND, NEW_DIRECTORY_COMMAND]


# noinspection PyShadowingNames
def main(current_directory):
	os.chdir(current_directory)
	while True:
		current_directory = os.getcwd()
		prompt = f"{USERNAME}@{PC_NAME}|{current_directory}> "
		command = get_command(prompt)
		command = command.split(' ')
		action = command[0]
		try:
			description = command[1]
		except IndexError:
			description = ""
		if action in COMMAND_LIST:
			if action == GO_TO_DIRECTORY_COMMAND:
				GoToDirectoryCommand(description).exec()
			
			if action == GO_TO_PARENT_DIRECTORY_COMMAND:
				if not (current_directory == 'C:\\'):
					GoToParentDirectoryCommand().exec()
			
			if action == NEW_DIRECTORY_COMMAND:
				NewDirectoryCommand(description).exec()
			
			if action == REMOVE_DIRECTORY_COMMAND:
				RemoveDirectoryCommand(description).exec()
			
			if action == EXECUTE_COMMAND:
				ExecuteCommand(description).exec()
			
		else:
			print(dye(f"Command '{action}' does not exist\n"
					  f"To see the list of applicable commands, please check out the project README\n"
					  f"or use the following command\n\n"
					  f"\tdemix -cmd\n"))

if __name__ == '__main__':
	main(current_directory)

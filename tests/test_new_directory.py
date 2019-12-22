from commands.directory_commands.new_directory import NewDirectoryCommand
import os

def test_new_directory_command_non_existing_folder():
	path = 'C:\\Users\\parsa'
	new_folder_name = 'peekaboo'
	os.chdir(path)
	NewDirectoryCommand(new_folder_name)
	assert new_folder_name in os.listdir(path)


def test_new_directory_command_existing_folder():
	path = 'C:\\Users\\parsa'
	new_folder_name = 'projects'
	os.chdir(path)
	NewDirectoryCommand(new_folder_name).exec()
	assert new_folder_name in os.listdir(path)

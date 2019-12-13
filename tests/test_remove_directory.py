from commands.directory_commands.remove_directory import RemoveDirectoryCommand
import os

def test_remove_directory_removable_directory():
	useless_dir_name = 'i-am-useless'
	os.mkdir(os.path.join(os.getcwd(), useless_dir_name))
	RemoveDirectoryCommand(useless_dir_name).exec()
	assert not useless_dir_name in os.listdir(os.getcwd())

def test_remove_directory_non_existing_directory():
	non_existing_directory_name = "i-am-not-real"
	RemoveDirectoryCommand(non_existing_directory_name).exec()
	assert not non_existing_directory_name in os.listdir(os.getcwd())

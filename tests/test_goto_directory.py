from commands.directory_commands.goto_directory import GoToDirectoryCommand
import os

def test_goto_directory_existing_directory():
	directory_name = '.pytest_cache'
	GoToDirectoryCommand(directory_name).exec()
	assert os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix\\tests\\{directory_name}"

def test_goto_directory_non_accessible_directory():
	directory_name = 'hack'
	GoToDirectoryCommand(directory_name).exec()
	assert not os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix\\tests\\{directory_name}"

def test_goto_directory_space_in_name():
	os.chdir("C:\\Users\\parsa\\projects\\Demix\\tests")
	directory_name = 'test..dir'
	GoToDirectoryCommand(directory_name).exec()
	assert os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix\\tests\\{directory_name.replace('..', ' ')}"

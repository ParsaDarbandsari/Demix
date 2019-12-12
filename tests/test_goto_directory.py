from command.directory_commands import GoToDirectoryCommand
import os

os.chdir("C:\\Users\\parsa\\projects\\Demix\\tests")

def test_goto_directory_existing_directory():
	directory_name = '.pytest_cache'
	GoToDirectoryCommand(directory_name).exec()
	assert os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix\\tests\\{directory_name}"

def test_goto_directory_non_accessible_directory():
	directory_name = 'hack'
	GoToDirectoryCommand(directory_name).exec()
	assert not os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix\\tests\\{directory_name}"

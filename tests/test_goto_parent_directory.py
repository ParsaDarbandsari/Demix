from commands.directory_commands.goto_parent_directory import GoToParentDirectoryCommand
import os

def test_goto_parent_directory_command_executable():
	os.chdir("C:\\Users\\parsa\\projects\\Demix\\tests")
	GoToParentDirectoryCommand(os.getcwd()).exec()
	assert os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix"

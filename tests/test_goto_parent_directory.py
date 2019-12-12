from command.directory_commands import GoToParentDirectoryCommand
import os

def test_goto_parent_directory_command_executable():
	GoToParentDirectoryCommand().exec()
	assert os.getcwd() == f"C:\\Users\\parsa\\projects\\Demix\\tests"

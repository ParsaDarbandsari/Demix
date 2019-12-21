from commands.directory_commands.goto_parent_directory import GoToParentDirectoryCommand
from commands.directory_commands.goto_directory import GoToDirectoryCommand
from commands.directory_commands.new_directory import NewDirectoryCommand
from commands.directory_commands.remove_directory import RemoveDirectoryCommand
from commands.directory_commands.list_directory import ListDirectoryCommand
from commands.execute_command import ExecuteCommand
from commands.command import Command

class DemixCommands(Command):
	cmd = 'demix'
	commands = (GoToDirectoryCommand, GoToParentDirectoryCommand, NewDirectoryCommand, RemoveDirectoryCommand, ListDirectoryCommand, ExecuteCommand)
	demix_commands = ('-cmd', '-author', '-version')
	usage = {
		'usage': 'demix [demix info]',
		'description': 'Shows you all the about demix(author, version.etc)'
	}
	
	def __init__(self, command):
		super(DemixCommands, self).__init__()
		if command == '-cmd':
			self.show_applicable_commands()
		else:
			print(self.usage['usage'])
	
	def show_applicable_commands(self):
		separator = (50, ' ')
		headers = {
			'name_header': 'NAME',
			'usage_header': 'USAGE',
			'description_header': 'DESCRIPTION'
		}
		
		print(f"{headers['name_header']}{' ' * (separator[0] - (len(headers['usage_header']) + 4))}{headers['usage_header']}  {headers['description_header']}")
		for cmd in self.commands:
			prompt = f""
			prompt += cmd.cmd
			prompt += separator[1] * (separator[0] - (len(cmd.usage['usage']) + len(cmd.cmd)))
			prompt += cmd.usage['usage'] + '\t'
			prompt += cmd.usage['description']
			
			print(prompt)

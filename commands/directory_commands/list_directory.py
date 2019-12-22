from commands.command import Command
from os import path
import time
import os


class ListDirectoryCommand(Command):
	cmd = 'list'
	usage = {
		'usage': 'list (no extra info needed)',
		'description': "Shows you a list of files and folders in your current directory"
	}
	
	def __init__(self, show_usage=False):
		super(ListDirectoryCommand, self).__init__()
		if not show_usage:
			self.exec()
		else:
			print(f"{self.usage['usage']}")
	
	def exec(self):
		directories = os.listdir(self.dir)
		spaces = (40, ' ')
		acceptable_file_length = spaces[0] - 5
		headers = {
			'name_header': 'NAME',
			'last_modified_time_header': 'LAST MODIFIED',
			'is_directory_header': '      '
		}
		
		print(f"{headers['name_header']}{spaces[1] * (spaces[0] - len(headers['name_header']))}{headers['is_directory_header']}{headers['last_modified_time_header']}")
		for entry in directories:
			prompt = ""
			last_modified = time.ctime(path.getmtime(entry))
			if len(entry) > acceptable_file_length:
				entry = entry[:acceptable_file_length]
				entry += '...'
			prompt += entry
			prompt += ' ' * (spaces[0] - len(entry))
			if os.path.isdir(entry):
				prompt += '<DIR> '
			else:
				prompt += ' ---  '
			prompt += last_modified
			print(prompt)

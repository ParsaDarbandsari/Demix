from commands.command import Command
from os import path
import time
import os


class ListDirectoryCommand(Command):
	cmd = 'list'
	def __init__(self):
		super(ListDirectoryCommand, self).__init__()
	
	def exec(self):
		directories = os.listdir(self.dir)
		spaces = 40
		acceptable_file_length = spaces - 5
		headers = {
			'name_header': 'NAME',
			'last_modified_time_header': 'LAST MODIFIED',
			'is_directory_header': '      '
		}
		
		print(f"{headers['name_header']}{' ' * (spaces - len(headers['name_header']))}{headers['is_directory_header']}{headers['last_modified_time_header']}")
		for entry in directories:
			prompt = ""
			last_modified = time.ctime(path.getmtime(entry))
			if len(entry) > acceptable_file_length:
				entry = entry[:acceptable_file_length]
				entry += '...'
			prompt += entry
			prompt += ' ' * (spaces - len(entry))
			if os.path.isdir(entry):
				prompt += '<DIR> '
			else:
				prompt += ' ---  '
			prompt += last_modified
			print(prompt)

class assistant:
	def __init__(self, name):
		self.name = name
	def say_name(self):
		print("Мое имя: ", self.name)

class program_assistant(assistant):
	def __init__(self, name, use):
		self.name = name
		self.use = use
		print('Вы добавили нового программного помощника: {0} с функцией: {1}' .format(name, use))

class robot_assistant(assistant):
	def __init__(self, name, use):
		self.name = name
		self.use = use
		print('Вы добавили нового робота помощника: {0} с функцией: {1}' .format(name, use))
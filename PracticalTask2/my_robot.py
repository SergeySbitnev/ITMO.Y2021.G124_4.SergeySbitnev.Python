class Robot:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print('Привет! Меня зовут', self.name)

class Robot_Cleaner(Robot):
	def __init__(self, name):
		Robot.__init__(self, name)
		self.use = 'cleaner'
		print('Создан работ уборщик: {0}' .format(self.name))
	def sayHi(self):
		Robot.sayHi(self)
		print('Назначение: {0}' .format(self.use))
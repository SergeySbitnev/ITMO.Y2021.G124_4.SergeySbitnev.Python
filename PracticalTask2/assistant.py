import time, csv, os
#Базовый класс для помощников
class assistant:
	def __init__(self, name):
		self.name = name
	def say_name(self):
		print("Мое имя: ", self.name)
#Базовый класс для работы с файлами
class work_file:
	#Добавить запись в файл
	def add_note(self, name):
		d = input('Дата(дд.мм.гггг): ')
		t = input('Время(чч:мм): ')
		subject = input('Тема: ')
	
		if os.path.exists(self.name + '.csv') == True:
			with open(self.name + '.csv', mode="a", encoding='utf-8') as w_file:
				names = ["Дата", "Время", "Тема"]
				file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
				file_writer.writerow({"Дата": d, "Время": t, "Тема": subject})
		else:
			with open(self.name + '.csv', mode="w", encoding='utf-8') as w_file:
				names = ["Дата", "Время", "Тема"]
				file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
				file_writer.writeheader()
				file_writer.writerow({"Дата": d, "Время": t, "Тема": subject})
	#Вывести все записи
	def show_records(self, name):
		try:
			with open(self.name + '.csv', encoding='utf-8') as r_file:
				file_reader = csv.DictReader(r_file, delimiter = ",")
				print('{0:15} {1:15} {2:15} '.format('Дата', 'Время', 'Тема'))
				for row in file_reader:
					print('{0:15} {1:15} {2:15}'.format(row["Дата"], row["Время"], row["Тема"]))
		except:
			print('Записи не найдены...')

#Класс программных помощников - Множественное наследование
class program_assistant(assistant, work_file):
	def __init__(self, name, use):
		self.name = name
		self.use = use
		print('Вы добавили нового программного помощника: {0} с функцией: {1}' .format(name, use))
	def add_meeting():
		print('Добавить встречу...')

	def meeting_list():
		print('Список встреч...')
#Класс роботизированных помощников
class robot_assistant(assistant):
	#Инициализация роботизированного помощника
	def __init__(self, name, use, length = 3, width = 3):
		self.name = name
		self.use = use
		self.length = length
		self.width = width
		print('Вы добавили нового робота помощника: {0} с функцией: {1}' .format(name, use))
	#Задание на уборку роботизированному помощнику
	def cleaner(self):
		print('Начало уборки... (загатовка для многопоточности)')
		for i in range(0, self.length*self.width):
			time.sleep(1)
			print('X')
#Класс исключения - если имя помощника уже существует
class found_name(Exception):
	def __intn__(self, text):
		self.text = text

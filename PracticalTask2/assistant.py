import time, csv, os
from tkinter import *
from tkinter import messagebox
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
		def new_add():
			if os.path.exists(self.name + '.csv') == True:
				with open(self.name + '.csv', mode="a", encoding='utf-8') as w_file:
					names = ["Дата", "Время", "Тема"]
					file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
					file_writer.writerow({"Дата": d.get(), "Время": t.get(), "Тема": subject.get()})
			else:
				with open(self.name + '.csv', mode="w", encoding='utf-8') as w_file:
					names = ["Дата", "Время", "Тема"]
					file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
					file_writer.writeheader()
					file_writer.writerow({"Дата": d.get(), "Время": t.get(), "Тема": subject.get()})
			messagebox.showinfo('Новая встреча', 'Новая встреча успешно добавлена!')
			d.delete(0, "end")
			t.delete(0, "end")
			subject.delete(0, "end")

		window = Tk()
		window.title('Добавить встречу')
		window.geometry('350x200')

		lbl_date = Label(window, text="Дата", width = 15)
		lbl_time = Label(window, text="Время")
		lbl_subject = Label(window, text="Тема")

		d = Entry(window, width=30)
		t = Entry(window, width=30)
		subject = Entry(window, width=30)

		button_add = Button(window, text="Добавить", command=new_add)
		button_exit = Button(window, text="Выход", command=window.destroy)

		lbl_date.grid(column=0,  row=0)
		d.grid(column=1,  row=0)
		lbl_time.grid(column = 0, row=1)
		t.grid(column=1,  row=1)
		lbl_subject.grid(column = 0, row=2)
		subject.grid(column=1,  row=2)

		button_add.place(x = 100,  y = 100)
		button_exit.place(x = 200,  y = 100)
		window.mainloop()

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
		print('{0} - начал уборку. После окончания вы получите соответствующее сообщение...'.format(self.name))
		for i in range(0, self.length*self.width):
			time.sleep(1)
		print('\n{0} - Закончил уборку'.format(self.name))
#Класс исключения - если имя помощника уже существует
class found_name(Exception):
	def __intn__(self, text):
		self.text = text

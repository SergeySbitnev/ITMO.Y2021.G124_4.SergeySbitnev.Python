import os, asyncio, time, random
from msvcrt import getch
from assistant import *
from threading import Thread

assistants = []
#Добавить помощника
def add_assist():
	otv =''
	while otv != '0':
		os.system('cls')
		list_assist(0)
		print('\n1. Добавить программного помощника по планированию')
		print('2. Добавить роботизированного помощника по уборке')
		print('0. Назад')
		otv = input('\nВыберите действие: ')

		if otv == '1' or otv == '2':
			try:
				name = input('\nВведите имя помощника: ')
				for item in assistants:
					if item.name == name:
						raise found_name('Помощник с таким именем уже существует.')
			except ValueError:
				print('Error type of value!')
			except found_name as e:
				print(e)
			else:
				if otv=='1':
					assistants.append(program_assistant(name, 'программа-планировщик'))
				if otv=='2':
					assistants.append(robot_assistant(name, 'робот-уборщик'))
			finish_def()
#Список помощников
def list_assist(key=1):
	os.system('cls')
	if len(assistants) != 0:
		print('Список помощников:')
		for i in range(len(assistants)):
			print('{0}. Имя: {1}, назначение: {2}' .format(i+1, assistants[i].name, assistants[i].use))
	else:
		print('У Вас нет ни одного помощника.')
	if key == 1:
		finish_def()
#Дать задание помощникам
def task_assist():
	otv = ''
	while otv != '0':
		os.system('cls')
		list_assist(0)
		print('0. Назад')
		otv = input('\nВыберите помощника или вернитесь на предыдущее меню: ')
		if len(assistants) != 0 and otv > '0' and otv <=str(len(assistants)):

			if str(type(assistants[int(otv)-1])) == "<class 'assistant.robot_assistant'>":
				thread1 = Thread(target = assistants[int(otv)-1].cleaner, args=())
				thread1.start()
				#assistants[int(otv)-1].cleaner()
			if str(type(assistants[int(otv)-1])) == "<class 'assistant.program_assistant'>":
				print('\n1. Добавить встречу')
				print('2. Просмотреть встречи')
				print('0. Назад')
				otv2 = input('\nВыберите действие: ')
				if otv2 == '1':
					assistants[int(otv)-1].add_note(assistants[int(otv)-1].name)
				if otv2 == '2':
					assistants[int(otv)-1].show_records(assistants[int(otv)-1].name)

			finish_def()

#Удалить помощника
def delete_assist():
	list_assist(0)
	if len(assistants) > 0:
		print('{0}. Асинхронное исключение всех помощников'.format(len(assistants)+1))
		print('0. Назад')
		otv = input('\nВыберите помощника которого необходимо исключить из работы: ')
		if otv > '0' and otv <= str(len(assistants)):
			del assistants[int(otv)-1]
			print('Помощник исключен...')
		elif otv == str(len(assistants)+1):
			print('\nАсинхронное исключение всех помощников:')
			asyncio.run(run_del_all())
		elif otv != '0':
			print('Не правильно выбран помощник. Попробуйте еще раз...')

	finish_def()
#Завершить работу программы
def exit():
	os.system('cls')
	print('Программа завершила работу.')
	finish_def()

#Конец функции
def finish_def():
	print('\nPress any key to continue...')
	getch()
#Функция для асинхронного удаления всех помощников
async def delete_all_assist(i):
	t = random.randint(2, 10)
	name = i.name
	print('Исключение помощника: {0}, это займет: {1} сек.'.format(name, t))
	await asyncio.sleep(random.randint(2, 10))
	assistants.remove(i)
	print('Помощник {0} исключен из работы.'.format(name))
#
async def run_del_all():
	all_assist = []
	for item in assistants:
		all_assist.append(asyncio.create_task(delete_all_assist(item)))
	for item in all_assist:
		await item
	all_assist.clear()

import os
from msvcrt import getch
from assistant import *

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

		if otv=='1':
			name = input('\nВведите имя помощника: ')
			assistants.append(program_assistant(name, 'программа-планировщик'))
			finish_def()
		if otv=='2':
			name = input('\nВведите имя помощника: ')
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
				assistants[int(otv)-1].cleaner()
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
		print('delete')

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
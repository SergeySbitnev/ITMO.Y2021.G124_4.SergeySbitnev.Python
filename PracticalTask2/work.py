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

def task_assist():
	print('task')
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
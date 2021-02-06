import os, work, datetime

def decorator_main_menu(function_to_decorate, menu):
	def around_function_todecorate():
		f = open('log.txt', 'a')
		f.write(str(datetime.datetime.now()) + ' start: ' + menu + '\r')
		f.close()
		function_to_decorate()
		f = open('log.txt', 'a')
		f.write(str(datetime.datetime.now()) + ' end: ' + menu + '\r')
		f.close()
	return around_function_todecorate()


def main_menu():
	otv = ''
	while otv != '0':
		os.system('cls')
		print('1. Добавить помощника')
		print('2. Список помощников')
		print('3. Дать задание помощнику')
		print('4. Удалить помощника')
		print('0. Завершить работу программы')
		otv = input('\nВыберите действие: ')
	
		if otv=='1':
			decorator_main_menu(work.add_assist, 'add_assist')
		if otv=='2':
			decorator_main_menu(work.list_assist, 'list_assist')
		if otv=='3':
			decorator_main_menu(work.task_assist, 'task_assist')
		if otv=='4':
			decorator_main_menu(work.delete_assist, 'delete_assist')

	work.exit()

decorator_main_menu(main_menu, '----------Running the program----------')
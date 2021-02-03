import os, work

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
		work.add_assist()
	if otv=='2':
		work.list_assist()
	if otv=='3':
		work.task_assist()
	if otv=='4':
		work.delete_assist()

work.exit()
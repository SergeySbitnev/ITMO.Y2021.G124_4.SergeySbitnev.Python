import os
import work

otv = ''
while otv != '0':
	os.system('cls')
	print('1. Add')
	print('2. Show all')
	print('3. Show for date')
	print('4. Show by category')
	print('5. Show by min->max')
	print('6. Delete')
	print('0. Exit')
	otv = input('What would you like to do? ')

	if otv=='1':
		work.add()
	if otv=='2':
		work.show_all()
	if otv=='3':
		work.show_for_date()
	if otv=='4':
		work.show_by_category()
	if otv=='5':
		work.show_by_min_max()
	if otv=='6':
		work.delete()

os.system('cls')
print('The work is over...')
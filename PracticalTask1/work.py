import os, csv
from msvcrt import getch
#Добавление покупки
def add():
	os.system('cls')
	print('Add product:')
	cat = input('Category: ')
	prod = input('Product: ')
	cost = input('Cost: ')
	date = input('Date(yyyy-mm-dd): ')

	if os.path.exists('purchase.csv') == True:
		with open('purchase.csv', mode="a", encoding='utf-8') as w_file:
			names = ["Category", "Product", "Cost", "Date"]
			file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
			file_writer.writerow({"Category": cat, "Product": prod, "Cost": cost, "Date": date})
	else:
		print('File not found. New file created...')
		with open('purchase.csv', mode="w", encoding='utf-8') as w_file:
			names = ["Category", "Product", "Cost", "Date"]
			file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
			file_writer.writeheader()
			file_writer.writerow({"Category": cat, "Product": prod, "Cost": cost, "Date": date})

	print('Product added.')
	print('Press any key to continue...')
	getch()
#Вывод всех покупок
def show_all():
	os.system('cls')
	try:
		with open('purchase.csv', encoding='utf-8') as r_file:
			file_reader = csv.DictReader(r_file, delimiter = ",")
			print('{0:15} {1:15} {2:15} {3:15}'.format('Category', 'Product', 'Cost', 'Date'))
			for row in file_reader:
				print('{0:15} {1:15} {2:15} {3:15}'.format(row["Category"], row["Product"], row["Cost"], row["Date"]))
	except:
		print('File not found...')

	print('Press any key to continue...')
	getch()
#Вывод покупок по дате
def show_for_date():
	os.system('cls')
	try:
		with open('purchase.csv', encoding='utf-8') as r_file:
			ch_date = input('Choose date(yyyy-mm-dd): ')
			file_reader = csv.DictReader(r_file, delimiter = ",")
			print('{0:15} {1:15} {2:15} {3:15}'.format('Category', 'Product', 'Cost', 'Date'))
			for row in file_reader:
				if row["Date"] == ch_date:
					print('{0:15} {1:15} {2:15} {3:15}'.format(row["Category"], row["Product"], row["Cost"], row["Date"]))
	except:
		print('File not found...')

	print('Press any key to continue...')
	getch()
#Вывод покупок по категории
def show_by_category():
	os.system('cls')
	try:
		with open('purchase.csv', encoding='utf-8') as r_file:
			ch_cat = input('Choose category: ')
			file_reader = csv.DictReader(r_file, delimiter = ",")
			print('{0:15} {1:15} {2:15} {3:15}'.format('Category', 'Product', 'Cost', 'Date'))
			for row in file_reader:
				if row["Category"] == ch_cat:
					print('{0:15} {1:15} {2:15} {3:15}'.format(row["Category"], row["Product"], row["Cost"], row["Date"]))
	except:
		print('File not found...')

	print('Press any key to continue...')
	getch()
#Вывод, отсортированного по возрастанию стоимости, списка покупок
def show_by_min_max():
	os.system('cls')
	try:
		with open('purchase.csv', encoding='utf-8') as r_file:
			file_reader = csv.DictReader(r_file, delimiter = ",")
			cat_list = []
			prod_list = []
			cost_list = []
			date_list = []
			for row in file_reader:
				cat_list.append(row["Category"])
				prod_list.append(row["Product"])
				cost_list.append(int(row["Cost"]))
				date_list.append(row["Date"])
			unite = list(zip(cat_list, prod_list, cost_list, date_list))
			unite.sort(key=lambda i: i[2])
			print('{0:15} {1:15} {2:15} {3:15}'.format('Category', 'Product', 'Cost', 'Date'))
			for row in unite:
				print('{0:15} {1:15} {2:15} {3:15}'.format(row[0], row[1], str(row[2]), row[3]))
	except:
		print('File not found...')

	print('Press any key to continue...')
	getch()
#Удаление списка
def delete():
	os.system('cls')
	try:
		otv_del = input('Delete shopping list(yes):')
		if otv_del =='yes':
			os.remove('purchase.csv')
			print('Shopping list deleted.')
		else:
			print('Shopping list not deleted.')
	except Exception as e:
		print('Error delete: ' + str(e))

	print('Press any key to continue...')
	getch()
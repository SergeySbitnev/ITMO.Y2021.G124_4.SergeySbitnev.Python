import datetime, shutil, os
name_files = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv']
log = open('log.txt', 'w')
for i in name_files:
	print(i)
	try:
		with open(i) as file:
			now_time = datetime.datetime.now()
			new_file = now_time.strftime("%d-%m-%Y %H%M%S") + '-' + i
			shutil.copyfile(i, new_file)
			log.write(str(now_time) + ': file ' + i + ' copied if file: ' + new_file + '\r')
			print('file copied')
	except Exception as e:
		log.write(str(now_time) + ': file ' + i + ' copied if file:' + str(e) + '\r')
		print(e)
log.close()

try:
	os.remove('log.txt')
	print('Log file remove.')
except Exception as e:
	print('Error remove: ' + str(e))
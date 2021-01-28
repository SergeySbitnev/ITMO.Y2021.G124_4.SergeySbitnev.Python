from random import randint
num = [randint(1, 100) for i in range(0,20)]
print('Сгенерированные числа: ', num)
new = []
for item in num:
	new.append('H' if item > 50 else 'L')
print('Результат работы: ', new)


import names, random, numpy as np
name = np.array([''.join(names.get_first_name()) for _ in range(100)])
nameAM = []
nameElse = []
for item in name:
	if item[0] >= 'A' and item[0] <= 'M':
		nameAM.append(item)
	else:
		nameElse.append(item)


print('\nСгенерированные имена: ')
for item in name:
	print(item, end=' ')
print('\nИмена от A до M: ')
for item in nameAM:
	print(item, end=' ')
print('\nОстальные имена: ')
for item in nameElse:
	print(item, end=' ')


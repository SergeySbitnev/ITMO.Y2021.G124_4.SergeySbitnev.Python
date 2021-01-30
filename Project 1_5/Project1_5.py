#Функция выводит среднее значение температуры, исключая из предоставленного списка значение None
def average_temp(value_list):
	sum = 0
	new_list = [i for i in value_list if i != 'None']
	print('Очищенный список: ', new_list)
	for i in new_list:
		sum += int(i)
	print('Средняя температура: ', round(sum / len(new_list), 2))
#Функция вовращает кортеж из отсортированных списков: отрицательные по убванию, положительные по возрастанию
def sorted_tuple (value_list):
	neg_num = []
	pos_num = []
	for i in value_list:
		if i < 0:
			neg_num.append(i)
		else:
			pos_num.append(i)
	return sorted(neg_num, reverse = True), sorted(pos_num)
#Возведение в степень
def exponentiation(n, p):
	value = n
	for i in range(1, int(p)):
		value = value * n
	return value
#Возведение в степень - рекурсия
def exponentiation_recursion(n, p):
	if p == 0:
		return 1
	return n * exponentiation_recursion(n, p-1)
#Задание 1
temp_list = ['-3', 'None', '-5', '-5', '-6', '-6', 'None', '-7', '-8', '-7']
print(temp_list)
average_temp(temp_list)
print()
#Задание 2
num_list = [3, -2, 5, 4, -1, -5, -2, 1, 2, -4]
print('Входной список: ', num_list)
print('Кортеж из отсортированных списков: ', sorted_tuple(num_list))
print()
#Задание 3
num = int(input('Введите число: '))
power = int(input('Введите степень: '))
print('Обычное возведение в степень: ', exponentiation(num, power))
print('Рекурсивное возведение в степень', exponentiation_recursion(num, power))
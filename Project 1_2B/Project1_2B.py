from random import randint
name = ['молоко', 'кофе', 'хлеб', 'печенье', 'огурцы', 'сахар', 'яйца', 'мыло', 'соль', 'морковь']
cost = [randint(20, 100) for i in range(0,10)]
employee = [randint(100, 999) for i in range(0,10)]

unite = list(zip(name, cost, employee))
print(unite)
unite.sort(key=lambda i: i[2])
print('Товар\t\tЦена\t\tКод продавца', end=' ')
for item in unite:
	print()
	for itemIn in item:
		print(itemIn, end='\t\t')
	


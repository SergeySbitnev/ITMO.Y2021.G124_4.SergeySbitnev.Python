
cost = [20, 70, 90, 54, 41, 27, 11, 684, 74, 102]
price = []

print('Первоначальная стоимость:', end=' ')
for item in cost:
	print(item, end=' ')
	price.append(item+item*0.2)

print('\nСтоимость с наценкой:', end=' ')
for item in price:
	print(item, end=' ')

print('\n')
from random import randint
cost2 = [randint(1, 100) for i in range(1,10)]
price2 = list(map(lambda item: item + item*0.2, cost2))
print(cost2)
print(price2)
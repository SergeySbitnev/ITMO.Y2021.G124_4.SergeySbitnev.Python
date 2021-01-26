cost = [20, 70, 90, 54, 41, 27, 11, 684, 74, 102]
price = []

print('Первоначальная стоимость:', end=' ')
for item in cost:
	print(item, end=' ')
	price.append(item+item*0.2)

print('\nСтоимость с наценкой:', end=' ')
for item in price:
	print(item, end=' ')
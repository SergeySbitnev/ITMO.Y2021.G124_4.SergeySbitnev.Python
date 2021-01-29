import csv
quantity = []
price = []
freight = []
count = 0
with open('orderdata_sample.csv', encoding='utf-8') as r_file:
	file_reader = csv.DictReader(r_file, delimiter = ",")
	for row in file_reader:
		quantity.append(row["Quantity"])
		price.append(row["Price"])
		freight.append(row["Freight"])
		count += 1

with open('new_orderdata_sample.csv', mode="w", encoding='utf-8') as w_file:
	names = ["Quantity", "Price", "Freight", "Total"]
	file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator= "\r", fieldnames = names)
	file_writer.writeheader()
	for i in range(0, count):
		total = float(quantity[i]) * float(price[i]) + float(freight[i])
		file_writer.writerow({"Quantity": quantity[i], "Price": price[i], "Freight": freight[i], "Total": total})




#print(type(quantity[0]))


'''
, "Price", "Freight", "Total"
if count == 0:
			print(f'Файл содержит столбцы: {", ".join(row)}')
		a = float(row["Quantity"]) * float(row["Price"]) + float(row["Freight"])
		print(a)
		count += 1
	print(f'Всего в файле {count} строк.')

f = open('orderdata_sample.csv')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line, end=' ')
f.close()
'''
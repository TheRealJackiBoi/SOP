import openpyxl
import random

data = []

for i in range(100):
    number = random.randint(0, 9)
    data.append(number) 

print(data)

wb = openpyxl.Workbook()
wb.create_sheet(index=0, title="sheet1")
sheet = wb['sheet1']
tal = 1
for i in data:
	sheet['A' + str(tal)] = i
	tal += 1


wb.save('pythonrandom.xlsx')
wb.close()
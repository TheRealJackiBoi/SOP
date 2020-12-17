from scipy import stats
import numpy as np
import random
import openpyxl

data = []

for i in range(100):
    number = random.randint(1, 9.0)
    data.append(number) 

rvs = np.random.power(data,100)

print(rvs)

wb = openpyxl.Workbook()
wb.create_sheet(index=0, title="sheet1")
sheet = wb['sheet1']
tal = 1
for i in rvs:
	sheet['A' + str(tal)] = i
	tal += 1


wb.save('pythonpowerlastdist.xlsx')
wb.close()
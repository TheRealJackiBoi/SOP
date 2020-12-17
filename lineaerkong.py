import openpyxl
import time

#definere funktionen der definere hvilket sekund det er, og bruger modulus med m for at det er inde for grænsen
def seconds(m):
    result = time.localtime()
    return result.tm_sec % m

m = 10
c = 1

print(seconds(m))

def random(xold, top):
	sec = seconds(top)
	xnew = (sec * xold + c) % top
	return xnew

data = []
xold = random(0, m)
print(xold)
data.append(xold)

for i in range(99):
	  xold = random(xold, m)
	  data.append(xold)

numerator = list(range(1,101))
print(numerator)
print(data)



wb = openpyxl.Workbook()
wb.create_sheet(index=0, title="sheet1")
sheet = wb['sheet1']

tal = 1
for i in data:
	sheet['A' + str(tal)] = i
	tal += 1



wb.save('data.xlsx')


wb.close()


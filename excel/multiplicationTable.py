#! python3
# multiplicationTable.py - this program generates a multiplication table up to 6.

import openpyxl


column = ['B', 'C', 'D', 'E', 'F', 'G']
wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'].value

for i in range(2, 8):
	sheet['A'+str(i)] = i - 1


for i in range(1,7):
	sheet[column[i-1]+'1'] = i

for y in range (2,8): 
	temp = str(sheet['A'+str(y)].value)
	for x in range(1,7): 
		sheet[column[x-1]+str(y)] = '=' + temp + '*' + str(sheet[column[x-1]+'1'].value)

wb.save('mutlitplicationTable.xlsx')
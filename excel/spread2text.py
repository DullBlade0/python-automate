#! python3
# spread2text.py - This program opens a spreadsheet
# and writes the cells of column A into one text file,
# the cells of column B into another and so on.

import os, openpyxl

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb.active
fileNames = 'test'

print('Reading spreadsheets...')
for x in range(1, sheet.max_column+1):
	textFile = open(fileNames+str(x)+'.txt', 'w')
	for y in range(1, sheet.max_row+1):
		textFile.write(''+str(sheet.cell(row = y, column =x).value))
	textFile.close()

print('Spreadsheets copied...')
#! python3
#textToSpeadsheet.py

import os, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

for i, items in enumerate(os.listdir('C:\\Users\\Dullblade\\Documents\GitHub\python_automate\excel\\texts'), start = 1):
	file = open('texts\\'+items)
	fileContent = file.readlines()	
	for x, item in enumerate(fileContent, start = 1):
		sheet.cell(row = x, column = i).value = item

wb.save('testSpreadsheet.xlsx')
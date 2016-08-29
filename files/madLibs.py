#! python3
import os,re

textFile = open('text.txt')
textContent = textFile.read()

#Searches for all the madlibs
madlib = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
test = madlib.findall(textContent)
madlibNums = len(test)

for i in range(madlibNums):
	newWord = input('Enter a '+test[i]+': ')
	textContent = madlib.sub(newWord, textContent, 1)
	
print(textContent)
newFile = open('madlib.txt', 'w')
newFile.write(textContent)
textFile.close()
newFile.close()
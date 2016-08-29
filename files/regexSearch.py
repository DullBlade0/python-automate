import os, sys, re

regex = re.compile(r'.txt$')  

print('Insert regular expression to find: ')
regexInput = input()
regex2 = re.compile(str(regexInput))
files = os.listdir()  
newFiles = []


for text in files:
    if regex.search(text):
        newFiles.append(str(text))


for doc in newFiles:
   text = open(doc)
   textRead = text.read()
   textRead = regex2.findall(textRead)
   print(textRead)
   print('Finished with file: '+str(doc))
   text.close()
print('Finished the code')
   


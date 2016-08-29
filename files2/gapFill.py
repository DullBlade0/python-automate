#! python3
# gapFill.py
# Fills gaps with their numeration, ex. spam001.txt, spam002.txt, spam003.txt

#def numberAnalyzer:


import re, os, shutil
numbering = [0,0,0]
print('Insert the prefix you\'d like to search')
prefix = input()
regex1 = re.compile(r'^'+prefix+'\d\d\d.txt$')
#regex2 = re.compile(r'\d\d\d\.txt$')
folder = os.path.abspath(os.getcwd())
listGap = []
for foldername, subfolders, filenames in os.walk(folder):
    filenames.sort()
    for item in filenames:
        if regex1.search(item) is not None:
            listGap.append(item)
print(listGap)

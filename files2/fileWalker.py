#! python3
# fileWalker.py
# Script that walks through files looking for a certain extension

import os, re, shutil

currentDirectory = os.getcwd()
backupDirectory = currentDirectory + '/backupDirectory/'
folder = os.path.abspath(currentDirectory)
print('Insert the file extension you ish to copy: ')
expression = input()
regexExpression = r'' + expression
regex = re.compile(regexExpression)

for foldername, subfolders, filenames in os.walk(folder):
    os.chdir(foldername)
    for fileName in filenames:
        if regex.search(fileName) is not None:
            print('Copying %s to %s ...' % (fileName, backupDirectory+fileName))
            shutil.copy(fileName, '/home/jose/Documentos/fileWalkerBackup')
        else:
            print('%s ignored.' % (fileName))

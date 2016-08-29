#! python3
# Program that finds files with a size >= 100MB
#It's left up to the user if they want to delete it.

import os, shutil, send2trash

currentDirectory = os.getcwd()
folder = os.path.abspath(currentDirectory)
for foldername, subfolders, filenames in os.walk(folder):
    os.chdir(foldername)
    print('Current directory is %s' % (os.getcwd()))
    for item in filenames:
        if os.path.getsize(item) >= 1000000:
            print('%s size is %s do you want to delete it? (Y/n)'  % (item, os.path.getsize(item)))
            if input() == 'Y':
                send2trash.send2trash(item)
                print('File deleted...')
            else:
                print('File not deleted...')

import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    #os.walk regresa 3 valores: 
    #string de folder a mirar
    #string de folders en el folder
    #string de archivos en el folder
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
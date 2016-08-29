#! python3
#backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    #Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) #makes sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        #Verifies if the ZIP exists
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TO-DO: Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TO-DO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        print(foldername)
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')
backupToZip(os.getcwd())

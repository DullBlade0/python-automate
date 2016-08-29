#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to european DD-MM-YYYY

import shutil, os, re

#Regex that matches files with the american date format.__base__

datePattern = re.compile(r'''^(.*?) #all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          #  all text after the date
    ''', re.VERBOSE)
    
# TODO: Loop over the files in the working directory

for amerFilename in os.listdir():
    mo = datePattern.search(amerFilename)
# TODO: Skip files without a date.
    if mo == None:
        continue
# TODO: Get the different parts of the filename
    beforePart = mo.group(1)
    print(beforePart)
    monthPart = mo.group(2)
    print(monthPart)
    dayPart = mo.group(4)
    print(dayPart)
    yearPart = mo.group(6)
    print(yearPart)
    afterPart = mo.group(8)
    print(afterPart) 
    print(mo.groups())

# TODO: Form the European-style filename    
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
 
# TODO: Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
# TODO: Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename,euroFilename)
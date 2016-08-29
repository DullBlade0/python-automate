import csv
from datetime import datetime

#Gets the data out of the CSV file.
timeFile = open('timeSchedule.csv')
timeReader = csv.reader(timeFile)
timeData = list(timeReader)
reportFile = open('report.txt', 'w')

FMT = '%H:%M' #To write less on datetime.strptime

for info in timeData:
    timeDelta = datetime.strptime(info[1], FMT) - datetime.strptime(info[0], FMT)
    if len(info) == 3:
        reportFile.write(str(timeDelta)+' hours worked on day: '+info[2]+'\n')
    else:
        reportFile.write('Hours worked: '+str(timeDelta) + '\n') #For the case no day was given on csv file

timeFile.close()
reportFile.close()

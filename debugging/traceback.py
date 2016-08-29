import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorLog.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorLog.txt')

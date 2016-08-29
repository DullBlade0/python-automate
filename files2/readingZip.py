import zipfile, os
os.chdir(os.getcwd())
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
print(str(spamInfo.file_size))
print(str(spamInfo.compress_size))
exampleZip.close()
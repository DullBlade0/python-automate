#! python3
# Encripts every pdf in a folder and its subfolders using a provided password

import os, sys, PyPDF2
password = sys.argv[1]

print('The password for the pdfs will be...%s' % password)

for root, dirs, files in os.walk(os.getcwd()):
    print('The current directory is: %s' % root)
    if root.endswith('encrypted'):
        print('The folder ' + root + ' will be ignored.')
        continue
    for item in files:
        currentItem=os.path.join(root, item)
        print('The current currentItem is: %s' % currentItem)
        if currentItem.endswith('.pdf'):
            print('The current file to be encrypted will be...%s' %currentItem)
            pdfFile = open(currentItem, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(password)
            index = currentItem.find('.pdf')
            fileName = currentItem[:index] + '_encrypted' + currentItem[index:]
            resultPdf = open(fileName, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfTest = PyPDF2.PdfFileReader(open(fileName, 'rb'))
            print('Attempting to decrypt %s' % item)
            if pdfTest.isEncrypted:
                if pdfTest.decrypt(password) == 1:
                    print('%s successfully decrypted!' % item)
print('All files in the current directory and subdirectories encrypted!')
            
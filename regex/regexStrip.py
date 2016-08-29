import re

def regexStrip(sentence,linea):
    regStrip = re.compile(linea)
    return regStrip.sub('',sentence)

text = 'Hello world this string is used for a basic test.'
print('Insert the character to be removed from the string')
remove = input()
print(remove)
if remove == '':
    remove = r' '
print(regexStrip(text,remove))

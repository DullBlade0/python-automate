import pyperclip, re

text = str(pyperclip.paste())
passwordRegexLower = re.compile(r'[a-z]')      
passwordRegexUpper = re.compile(r'[A-Z]+')     
passwordRegexNumber = re.compile(r'[0-9]+')    
if (len(text) >= 8) and (passwordRegexLower.findall(text) and passwordRegexUpper.findall(text) and passwordRegexNumber.findall(text) != []):
    print('You got a secure password.')
else:
    print('You got an insecure password')



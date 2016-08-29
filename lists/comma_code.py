def agregar(lista):
    grupo = ''
    for i in lista:
        grupo += i
    return grupo

spam = ['apples','bananas','tofu','cats']
caja = agregar(spam)
print(caja)

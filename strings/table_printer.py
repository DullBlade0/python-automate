#table_printer.py
#prints a table of lists with the same amount of elements

#Function to print the table
def printTable(tableData):
    rowLength = 0
    colWidths = [0] * len(tableData)
    for i, column in enumerate(tableData):
        if(rowLength<len(column)):
            rowLength = len(column)
        for word in column:
            if(colWidths[i] < len(word)):
                colWidths[i] = len(word)
    for i in range(rowLength):
        tableRow=''
        for j, row in enumerate(tableData):
            tableRow+=row[i].rjust(colWidths[j])+' '
        print(tableRow)

#Main part of the program
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

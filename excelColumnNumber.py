def excelColumn(colNum):

    first = ord('A') - 1
    num = 0
    for i in colNum:
        
        num = num * 26 + ord(i) - first
        
    return num

print excelColumn('AA')
print excelColumn('KW')

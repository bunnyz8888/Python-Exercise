#Xuất file output trên 1 dòng từ chuỗi input bất kỳ nhập vào từ nhiều dòng
with open('12.input.txt', 'r', encoding='utf-8') as fileInp:
    data = fileInp.readlines()
    stringJoined = ' '.join(data).replace('\n', '')
fileOut = open('12.output.txt', 'wb')
fileOut.write(stringJoined.encode('utf8'))

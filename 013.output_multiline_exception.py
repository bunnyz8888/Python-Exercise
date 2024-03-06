#Xuất file output trên 1 dòng từ chuỗi input bất kỳ nhập vào từ nhiều dòng (Có xử lý ngoại lệ đầu vào)
try:
    with open('13.input.txt', 'r', encoding='utf-8') as fileInp:
        data = fileInp.readlines()
        stringJoined = ' '.join(data).replace('\n', '')
        danhSachCacTu = stringJoined.split()
        stringJoined = ' '.join(danhSachCacTu).replace('\n', '')
    fileOut = open('13.output.txt', 'wb')
    fileOut.write(stringJoined.encode('utf8'))
except:
    print('Lỗi file')

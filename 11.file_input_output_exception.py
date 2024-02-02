#Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output theo mẫu (Có xử lý định dạng đầu vào)
try:
    with open('10.input.txt', 'r', encoding = 'utf-8') as fileInp:
        #rstrip loại bỏ các ký tự xuống dòng trong chuỗi
        #readline đọc một dòng, readlines đọc nhiều dòng
        ten = fileInp.readline().rstrip('\n')
        tuoiHienTai = int(fileInp.readline().rstrip('\n'))
    with open('11.output_exception.txt', 'wb') as fileOut:
        stringToSave = '20 năm nữa, tuổi của {} sẽ là {}'.format(ten, tuoiHienTai + 20)
        fileOut.write(stringToSave.encode('utf8'))
except FileNotFoundError:
    print('Không tìm thấy file')
except:
    print('Đầu vào không hợp lệ')
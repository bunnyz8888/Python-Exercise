#Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output theo mẫu
with open('10.input.txt', 'r') as fileInp:
    #rstrip loại bỏ các ký tự xuống dòng trong chuỗi
    #readline đọc một dòng, readlines đọc nhiều dòng
    ten = fileInp.readline().rstrip('\n')
    tuoiHienTai = int(fileInp.readline().rstrip('\n'))
with open('10.output.txt', 'w') as fileOut:
    fileOut.write('20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))

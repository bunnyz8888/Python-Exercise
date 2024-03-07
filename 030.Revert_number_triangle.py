#Hiển thị tam giác số kích thước n với đầu nhọn hướng xuống
print ('Nhap kich thuoc tam giac mong muon')
try:
    n = int(input())

    if n < 1 or n > 9:
        print('Vui long nhap gia tri tu 1 toi 9')
    else:
        for i in range (n):
            line = ''
            for j in range (n - i, 0, -1):
                line = '{} {}'.format(line, j)
            print (line)
except:
    print('Loi dau vao')

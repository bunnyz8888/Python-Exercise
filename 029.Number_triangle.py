#Hiển thị ra màn hình tam giác số kích thước n
print ('Nhap kich thuoc tam giac mong muon')
try:
    n = int(input())

    if n < 1 or n > 9:
        print('Vui long nhap gia tri tu 1 toi 9')
    else:
        for i in range (1, n + 1):
            line = ''
            for j in range (1, i + 1):
                line = '{} {}'.format(line, j)
            print (line)
except:
    print('Loi dau vao')

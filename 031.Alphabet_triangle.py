#Hiển thị tam giác cân chứa các ký tự alphabet có kích thước n
try:
    n = int(input())
    if n < 0:
        print('Vui long nhap so tu nhien')
    else:
        maAscii = 65
        for i in range(n):
            khoangTrangDauDong = ' ' * ((n-i)*2)
            print(khoangTrangDauDong, end = ' ')
            
            for j in range(2*i+1):
                chuCai = chr(maAscii)
                print(chuCai, end = ' ')
                maAscii += 1

                if(chr(maAscii) > 'Z'):
                    maAscii = 65
            print()
except:
    print('Loi dau vao')

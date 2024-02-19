#Tính tổng các số nguyên trong khoảng a đến b. (Vòng lặp while)
try:
    print ('Nhap so thu nhat')
    a = int(input())
    print ('Nhap so thu hai')
    b = int(input())

    if a > b:
        print ('So thu nhat phai nho hon so thu hai')
    else:
        tong = 0
        i = a
        while i <= b:
            tong += i
            i += 1
        print ('Tong: {}'.format(tong))
except:
    print('Loi dau vao')
#Hiển thị 10 số chia hết cho 5 trong khoảng a, b (a <= b)
try:
    print ('Nhap so thu nhat')
    a = int(input())
    print ('Nhap so thu hai')
    b = int(input())
    if a > b:
        print ('So thu nhat phai nho hon so thu hai')
    else:
        dem = 0
        for i in range (a, b):
            if i % 5 == 0:
                print('So chia het cho 5 gom:', i)
                dem += 1
                if dem > 10:
                    break
except:
    print('Co loi dau vao')
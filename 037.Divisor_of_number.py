#Hiển thị tất cả các ước của một số tự nhiên n nhập từ bàn phím
n = int(input())

if n < 0:
    print('Vui long nhap so nguyen duong')
else:
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
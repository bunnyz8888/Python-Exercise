#Tính và hiển thị số Fibonacci thứ n (Với n là số tự nhiên nhập từ bàn phím)
n = int(input())

if n <= 0:
    print('Vui long nhap so nguyen duong')
elif n == 1 or n == 2:
    print(1)
else:
    soThuNhat, soThuHai = 1, 1
    for i in range(n-2):
        soThuNhat, soThuHai = soThuHai, soThuNhat + soThuHai
    print('So fibonacci thu n la {}'.format(soThuHai))
#Tính và hiển thị ra màn hình n giai thừa (n!)
n = int(input())

if n < 0:
    print('Nhap gia tri lon hon 0')
else:
    giaiThua = 1
    for i in range(1, n+1):
        giaiThua *= i
    print('Gia tri cua {}! la {}'.format(n,giaiThua))
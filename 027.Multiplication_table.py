#Hiển thị ra màn hình bảng cửu chương n (1<=n<=9)
print('Nhap bang cuu chuong muon tinh')
try:
    n = int(input())

    if n < 1 or n > 9:
        print('Chi tinh bang cuu chuong tu 1 den 9')
    else:
        for i in range (1, 10):
            print('{} x {} = {}'.format(n, i, n*i))
except:
    print('Co loi dau vao')

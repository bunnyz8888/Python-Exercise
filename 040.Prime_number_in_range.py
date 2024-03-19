#Hiển thị ra màn hình các số nguyên tố trong đoạn từ a đến b. (Với a <= b, a,b là số nguyên tố)
import math
a = int(input())
b = int(input())

if a < 0 or b < 0:
    print('Vui long nhap so nguyen duong')
elif a > b:
    print('So thu hai phai lon hon so thu nhat')
else:
    for n in range(a, b+1):
        if n < 2:
            continue
        for i in range (2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            print(n, end=' ')

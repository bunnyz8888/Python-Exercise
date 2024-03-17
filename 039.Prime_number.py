#Kiểm tra n có phải số nguyên tố không. (Với n là số tự nhiên)
import math
n = int(input())

if n < 0:
    print('Vui long nhap so nguyen duong')
elif n < 2:
    print('{} khong la so nguyen to'.format(n))
else:
    #for i in range (2, n//2 + 1):
    #Không cần duyệt tới n/2 chỉ cần duyệt tới căn bậc hai của n 
    #=> Tối ưu và tốn ít tài nguyên hơn
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print('{} khong la so nguyen to'.format(n))
            break
    else:
        print('{} la so nguyen to'.format(n))
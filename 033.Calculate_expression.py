#Tính S(n) = 1 - x + x^2/2! - x^3/3! + … - x^(2n-1)/(2n-1)! + x^(2n)/(2n)!
print('Nhap gia tri cua n')
n = int(input())
print('Nhap gia tri cua x')
x = float(input())

if n < 0:
    print ('Vui long nhap so lon hon 0')
elif n == 0:
    print(1)
else:
    S = 1
    giaiThua = 1
    for i in range(1, 2*n+1):
        giaiThua *= i
        if i % 2 == 0:
            S += pow(x, i)/giaiThua
        else:
            S -= pow(x, i)/giaiThua
    print('{:.5f}'.format(S))

#Kiểm tra n có phải số hoàn hoàn thiện không. Với n là số nguyên dương
n = int(input())

if n < 0:
    print('Vui long nhap so nguyen duong')
else:
    tongUoc = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            tongUoc += i
    if n == tongUoc:
        print('{} la so hoan thien'.format(n))
    else:
        print('{} khong la so hoan thien'.format(n))
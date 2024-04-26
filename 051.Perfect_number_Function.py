#Viết hàm liệt kê các số hoàn thiện nhỏ hơn n
def kiem_tra_so_hoan_thien(n):
    tongUoc = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            tongUoc += i
    if n == tongUoc:
        return True
    return False

def liet_ke_so_hoan_thien(n):
    for i in range(1, n):
        if kiem_tra_so_hoan_thien(i):
            print(i, end = ' ')


n = int(input())

if n < 0:
    print('Vui long nhap so nguyen duong')
else:
    liet_ke_so_hoan_thien(n)
    
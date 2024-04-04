#Viết hàm giải phương trình bậc nhất và phương trình bậc hai
import math
def menu():
    print('Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai')

def ptBac1(a, b):
    if a == 0:
       if b == 0:
           return "Phuong trinh co vo so nghiem"
       return "Phuong trinh vo nghiem"
    return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

def ptBac2(a, b, c):
    if a == 0:
       return ptBac1(b, c)
    delta = b * b - 4 * a * c
    if delta > 0:
       x1 = float((-b + math.sqrt(delta)) / (2 * a))
       x2 = float((-b - math.sqrt(delta)) / (2 * a))
       return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
    if delta == 0:
       x = -b / (2 * a)
       return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
    return "Phuong trinh vo nghiem"

menu()
try:
    chucNang = input()

    if chucNang == '1':
        a, b = map(float, input().split())
        print(ptBac1(a, b))
    elif chucNang == '2':
        a, b, c = map(float, input().split())
        print(ptBac2(a, b, c))
    else:
        menu()
except:
    print("Dinh dang dau vao khong hop le!")

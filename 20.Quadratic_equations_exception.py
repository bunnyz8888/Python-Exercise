#Giải phương trình bậc hai (Có xử lý ngoại lệ đầu vào)
import math
print ('Nhap 3 he so cach nhau boi dau cach')
duLieu = False
try:
    a, b, c = map(float, input().split())
    duLieu = True
except:
    print ('Co loi du lieu dau vao')
if duLieu:
    if a == 0:
        if b == 0:
            if c == 0:
                print ('Phuong trinh co vo so nghiem')
            else:
                print ('Phuong trinh vo nghiem')
        else:
            print ('Phuong trinh co 1 nghiem duy nhat: \nx = {}'.format(-c/b))
    else:
        delta = b*b - 4*a*c
        if delta > 0:
            x1 = float((-b + math.sqrt(delta)) / (2 * a))
            x2 = float((-b - math.sqrt(delta)) / (2 * a))
            print ("Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2))
        elif delta == 0:
            x = -b / (2 * a)
            print("Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x))
        else:
            print("Phuong trinh vo nghiem")

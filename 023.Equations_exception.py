#Giải phương trình bậc nhất và bậc hai (Có xử lý ngoại lệ đầu vào)
import math
try:
    with open('23.Input.txt', 'r') as fileInp:
        dongDauTien = fileInp.readline().strip()
        if dongDauTien == '1':
            dongThuHai = fileInp.readline()
            a, b = map(float, dongThuHai.split())
            if a == 0:
                if b ==0:
                    thongBao = "Phuong trinh co vo so nghiem"
                else:
                    thongBao = "Phuong trinh vo nghiem"
            else:
                thongBao = 'Phuong trinh co nghiem duy nhat: \nx = {}'.format(-b/a)
        elif dongDauTien == '2':
            dongThuHai = fileInp.readline()
            a, b, c = map(float, dongThuHai.split())
            if a == 0:
                if b == 0:
                    if c == 0:
                        thongBao = 'Phuong trinh co vo so nghiem'
                    else:
                        thongBao = 'Phuong trinh vo nghiem'
                else:
                    thongBao ='Phuong trinh co 1 nghiem duy nhat: \nx = {}'.format(-c/b)
            else:
                delta = b*b - 4*a*c
                if delta > 0:
                    x1 = float((-b + math.sqrt(delta)) / (2 * a))
                    x2 = float((-b - math.sqrt(delta)) / (2 * a))
                    thongBao = "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
                elif delta == 0:
                    x = -b / (2 * a)
                    thongBao = "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
                else:
                    thongBao = "Phuong trinh vo nghiem"
        else:
            thongBao = 'Vui long chon 1 hoac 2'
except FileNotFoundError:
   thongBao = "Khong tim thay file input!"
except:
   thongBao = "Dinh dang dau vao khong hop le!"

with open('23.Output.txt', 'w') as fileOut:
    fileOut.write(thongBao)

#Nhập file input và xác định loại tam giác
try:
   with open('22.Input.txt', 'r') as fileInp:
       dongDauTien = fileInp.readline().rstrip('\n')
   a, b, c = map(float, dongDauTien.split())

   if a<=0 or b<=0 or c<=0:
       thongBao = "Cac canh cua tam giac phai lon hon 0!"
   elif a+b>c and a+c>b and b+c>a:
       if a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b:
           loaiTamGiac = 'vuong'
       elif a==b and b==c:
           loaiTamGiac = 'deu'
       elif a==b or a==c or b==c:
           loaiTamGiac = 'can'
       elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
           loaiTamGiac = 'tu'
       else:
           loaiTamGiac = 'nhon'
       thongBao = "{}, {}, {} la ba canh cua mot tam giac {}".format(a, b, c, loaiTamGiac)
   else:
       thongBao = "{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c)

#Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
   thongBao = "Khong tim thay file input!"

#Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"
except:
   thongBao = "Dinh dang dau vao khong hop le!"

#Mo file voi mode='w' de ghi file
with open('22.Output.txt', 'w') as fileOut:
   #Xuat thong bao ra file out
   fileOut.write(thongBao)

#Tính và xuất kết quả máy tính đơn giản với hai số
print ('Nhap 2 so va phep tinh cach nhau boi dau cach')
try:
   soThu1, phepTinh, soThu2 = input().split()
   soThu1 = float(soThu1)
   soThu2 = float(soThu2)
   ketQua = None

   if phepTinh == '+':
      ketQua = soThu1 + soThu2
   elif phepTinh == '-':
      ketQua = soThu1 - soThu2
   elif phepTinh == 'x':
      ketQua = soThu1 * soThu2
   elif phepTinh == ':':
      if soThu2 == 0:
         print("So chia phai khac 0!")
      else:
         ketQua = soThu1 / soThu2

   if ketQua != None:
      print("{} {} {} = {}".format(soThu1, phepTinh, soThu2, ketQua))
except:
   print('Loi dau vao')

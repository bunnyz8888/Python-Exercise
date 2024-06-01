#Hiển thị số lần xuất hiện của các ký tự trong chuỗi s. (Với tham số là chuội s)
def dem_ky_tu(s):
   #Set constructor
   setKyTu = set(s)

   #Su dung vong lap for de duyet cac ky tu
   for kyTu in setKyTu:
       #Su dung phuong thuc count() de dem so lan xuat hien trong chuoi s
       dem = s.count(kyTu)
       #Hien thi ra man hinh
       print("'{}': {}; ".format(kyTu, dem), end='')

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
dem_ky_tu(s)

#Viết hàm hiển thị ra màn hình tên và quốc tịch tương ứng với vị trí trong danh sách. (Tham số là 2 danh sách)
def xoa_khoang_trang_thua(s):
   #Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
   s = s.strip()
   #Su dung vong lap while de lap cho toi khi nao het khoang trang thua
   while "  " in s:
       #Su dung phuong thuc replace() de thay the 2 khoang trang thanh 1 khoang trang
       s = s.replace("  ", " ")
   return s

def in_danh_sach(dsTen,  dsQuocTich):
   #Su dung List Comprehension de xoa cac khoang trang thua cua cua phan tu
   dsTen = [xoa_khoang_trang_thua(ten) for ten in dsTen]
   dsQuocTich = [xoa_khoang_trang_thua(quocTich) for quocTich in dsQuocTich]
   #Su dung vong lap for voi ham zip() de ghep 2 chuoi voi nhau
   for ten, quocTich in zip(dsTen, dsQuocTich):
       print(ten + " - " + quocTich)

#Nhap danh sach tu ban phim
#Su dung ham split(',') de cat chuoi dua vao dau ','
dsTen = input().split(',')
dsQuocTich = input().split(',')

#Kiem tra danh sach co cung kich thuoc hay khong
if len(dsTen) != len(dsQuocTich):
   print("Vui long nhap hai danh sach cung kich thuoc!")
else:   
   #Goi ham va truyen cac tham so can thiet
   in_danh_sach(dsTen, dsQuocTich)

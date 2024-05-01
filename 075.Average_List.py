#Viết hàm trả về trung bình cộng của danh sách đó. (Với tham số là danh sách số thực)
def trung_binh_cong(danhSach):
   tongDanhSach = sum(danhSach)
   soPhanTu = len(danhSach)
   trungBinhCong = tongDanhSach/soPhanTu
   return trungBinhCong

#Nhap danh sach tu ban phim
danhSach = input().split()
#Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   #Khoi lenh co the phat sinh loi
   try:
       #Ep kieu du lieu sang so thuc
       danhSachSo = list(map(float, danhSach))
       #Goi thuc thi ham va truyen tham so cho ham
       trungBinhCong = trung_binh_cong(danhSachSo)
       print(trungBinhCong)
   #Khoi lenh duoc thuc thi khi loi xay ra
   except:
       print("Vui long nhap cac phan tu la so thuc!")

#Viết hàm trả về trung bình cộng và hai danh sách số nhỏ hơn & số lớn hơn hoặc bằng TBC. (Tham số là hai danh sách số thực).
def tach_danh_sach(danhSachSo):
   trungBinhCong = sum(danhSachSo) / len(danhSachSo)   
   dsNhoHon = [so for so in danhSachSo if so < trungBinhCong]
   dsLonHon = [so for so in danhSachSo if so >= trungBinhCong]
   return trungBinhCong, dsNhoHon, dsLonHon

#Nhap danh sach tu ban phim
danhSach = input().split()
#Khoi lenh co the phat sinh loi
try:
   #Ep kieu du lieu sang so thuc
   danhSachSo = list(map(float, danhSach))
   #Goi thuc thi ham va truyen tham so cho ham
   trungBinhCong, dsNhoHon, dsLonHon = tach_danh_sach(danhSachSo)
   print(trungBinhCong)
   #Unpacking arguments
   print(*dsNhoHon)
   print(*dsLonHon)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Vui long nhap cac phan tu la so thuc!")

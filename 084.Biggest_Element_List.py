#Viết hàm trả về giá trị, số lượng và vị trí xuất hiện của phần tử lớn nhất trong danh sách. (Tham số là danh sách các số thực)
def phan_tu_lon_nhat(danhSachSo):
   giaTri = max(danhSachSo)
   soLuong = danhSachSo.count(giaTri)
   dsViTri = [vt for vt in range(0, len(danhSachSo)) if danhSachSo[vt] == giaTri]
   return giaTri, soLuong, dsViTri

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
       giaTri, soLuong, dsViTri = phan_tu_lon_nhat(danhSachSo)
       print(giaTri)
       print(soLuong)
       #Unpacking arguments
       print(*dsViTri)

   #Khoi lenh duoc thuc thi khi loi xay ra
   except:
       print("Vui long nhap cac phan tu la so thuc!")

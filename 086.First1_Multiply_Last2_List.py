#Viết hàm trả về danh sách kết quả nhân số đầu tiên của danh sách 1 với số cuối cùng của danh sách 2 . (Tham số là 2 danh sách)
def nhan_hai_danh_sach(danhSach1, danhSach2):
   #Su dung Comprehension va ham zip() de ghep 2 chuoi
   dsKetQua = [so1*so2 for so1, so2 in zip(danhSach1, danhSach2[::-1])]

   # for so1, so2 in zip(danhSach1, danhSach2[::-1]):
   #     dsKetQua.append(so1*so2)
   return dsKetQua


#Nhap danh sach tu ban phim
danhSach1 = input().split()
danhSach2 = input().split()
#Kiem tra xem danh sach co rong hay khong
if len(danhSach1) != len(danhSach2):
   print("Vui long nhap hai danh sach cung kich thuoc!")
else:
   #Khoi lenh co the phat sinh loi
   try:
       #Ep kieu du lieu sang so thuc
       danhSach1 = list(map(float, danhSach1))
       danhSach2 = list(map(float, danhSach2))
       #Goi thuc thi ham va truyen tham so cho ham
       dsKetQua = nhan_hai_danh_sach(danhSach1, danhSach2)
       #Unpacking arguments
       print(*dsKetQua)

   #Khoi lenh duoc thuc thi khi loi xay ra
   except:
       print("Vui long nhap cac phan tu la so thuc!")

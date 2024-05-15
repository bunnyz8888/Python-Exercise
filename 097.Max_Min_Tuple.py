#Viết hàm trả về giá trị lớn nhất, giá trị nhỏ nhất, số phần tử tuple. (Tham số là tuple bất kỳ)
def thong_tin_tuple(tupleX):
   return max(tupleX), min(tupleX), len(tupleX)

#Nhap danh sach tu ban phim
danhSach = input().split()
#Khoi lenh co the phat sinh loi
try:
   #Ep kieu du lieu sang so thuc va tra ve tuple
   tupleSo = tuple(map(float, danhSach))
   #Goi thuc thi ham va truyen tham so cho ham
   soLonNhat, soNhoNhat, soPhanTu = thong_tin_tuple(tupleSo)
   #Hien thi cac ket qua theo dinh dang dau ra yeu cau
   print(soLonNhat)
   print(soNhoNhat)
   print(soPhanTu)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Vui long nhap cac phan tu la so thuc!")

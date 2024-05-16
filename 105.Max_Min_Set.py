#Trả về giá trị lớn nhất, giá trị nhỏ nhất và tổng các phần tử của set. (Với tham số là set gồm các số thực)
def thong_tin_set(setX):
   return max(setX), min(setX), sum(setX)

#Nhap danh sach tu ban phim
danhSach = input().split()
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   #Khoi lenh co the phat sinh loi
   try:
       #Ep kieu du lieu sang so thuc va tra ve set
       #Set constructor
       setX = set(map(float, danhSach))
       #Goi thuc thi ham va truyen tham so cho ham
       thongTinSet = thong_tin_set(setX)
       #Hien thi cac ket qua theo dinh dang dau ra yeu cau
       print(*thongTinSet, sep='\n')
   #Khoi lenh duoc thuc thi khi loi xay ra
   except:
       print("Vui long nhap cac phan tu la so thuc!")

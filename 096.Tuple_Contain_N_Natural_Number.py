#Viết hàm trả về tuple gồm 2 phần tử là: số tự nhiên n và tuple chứa n số tự nhiên n. (Tham số tự nhiên n)
def khoi_tao_tuple(n):
   tupleCon = tuple(n for _ in range(n))
   tupleKetQua = (n, tupleCon)
   return tupleKetQua

#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop M, N <=0
   if n < 0:
       print("Vui long nhap so nguyen duong!")
   else:
       #Goi thuc thi ham va truyen tham so cho ham
       ketQua = khoi_tao_tuple(n)
       print(ketQua)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

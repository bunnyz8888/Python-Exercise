#Viết hàm khởi tạo và hiển thị tuple chứa n tự nhiên đầu tiên ra màn hình
def tuple_so_tu_nhien(n):
   tupleSTN = tuple(i for i in range(n))
   print(tupleSTN)

#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n < 0
   if n < 0:
       print("Vui long nhap so nguyen duong!")
   else:
       #Goi thuc thi ham va truyen tham so cho ham
       tuple_so_tu_nhien(n)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

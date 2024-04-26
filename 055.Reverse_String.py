#Trả về chuỗi con đảo ngược từ vị trí a đến b của chuỗi S
def chuoi_con_dao_nguoc(s, a, b):
   #Cat chuoi con tu vi tri a den vi tri b
   chuoiCon = s[a:b+1]
   #Dao nguoc chuoi con
   chuoiConDaoNguoc = chuoiCon[::-1]
   return chuoiConDaoNguoc

try:
   #Nhap cac gia tri dau vao tu ban phim
   s = input()
   a, b = map(int, input().split())

   #Su dung cau truc re nhanh xu ly cac truong hop ngoai le
   if a < 0 or b < 0:
       print("Vui long nhap a, b la so tu nhien!")
   elif a > b:
       print("Vui lonng nhap a <= b")
   elif a >= len(s) or b >= len(s):
       print("a, b lon hon do dai cua chuoi!")
   else:
       #Goi ham xu ly va truyen cac tham so can thiet
       print(chuoi_con_dao_nguoc(s, a, b))

#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

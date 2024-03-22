#Hiển thị câu theo mẫu (Với tham số là {Ten} và {Tuoi} )
def xin_chao(ten, tuoi):
   print("Xin chao! Toi la {}, toi {} tuoi.".format(ten, tuoi))

try:
   ten = input()
   tuoi = int(input())
  
   if tuoi < 0:
       print("Vui long nhap tuoi la so nguyen duong!")
   else:   
       xin_chao(ten, tuoi)
except:
   print("Dinh dang dau vao khong hop le!")

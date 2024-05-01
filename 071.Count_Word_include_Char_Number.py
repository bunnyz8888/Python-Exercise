#Viết hàm trả về số lượng từ vừa chứa ký tự, vừa chứa chữ số trong chuỗi s
def dem_tu(s):
   dem = 0
   #Su dung phuong thuc split() de cat chuoi s thanh cac tu ngan cach bang khoang trang
   dsCacTu = s.split()

   #Su dung vong lap for de duyet cac tu trong danh sach cac tu cua chuoi s
   for tu in dsCacTu:
       coKyTu = False
       coChuSo = False

       #Duyet cac ky tu trong tu
       for kyTu in tu:
           #Kiem tra ky tu
           if kyTu.isalpha():
               coKyTu = True
           #Kiem tra chu so
           if kyTu.isdigit():
               coChuSo = True

       #Neu tu vua chua ky tu vua chua chu so thi tang bien dem
       if coKyTu and coChuSo:
           dem += 1
   return dem
  
#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
print(dem_tu(s))

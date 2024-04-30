#Hàm hiển thị các câu của chuỗi s. Các câu đã xóa khoảng trắng thừa và định dạng theo tittle()
def xoa_khoang_trang_thua(s):
   #Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
   s = s.strip()
   #Su dung vong lap while de lap cho toi khi nao het khoang trang thua
   while "  " in s:
       #Su dung phuong thuc replace() de thay the 2 khoang trang thanh 1 khoang trang
       s = s.replace("  ", " ")
   return s

def hien_thi_cau(s):
   #Su dung phuong thuc split() de cat chuoi s thanh cac cau ngan cach bang dau cham
   dsCacCau = s.split('.')
   #Su dung vong lap for de duyet cau trong danh sach cac cau cua chuoi s
   for cau in dsCacCau:
       #Goi ham xoa khoang trang thua
       cau = xoa_khoang_trang_thua(cau)
       #Hien thi ra man hinh cau voi dinh dang title()
       print(cau.title())

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
hien_thi_cau(s)

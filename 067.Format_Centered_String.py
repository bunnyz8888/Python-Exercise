#Viết hàm hiển thị các câu của chuỗi s đã được xóa khoảng trắng thừa và căn giữa theo câu dài nhất
def xoa_khoang_trang_thua(s):
   #Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
   s = s.strip()
   #Su dung vong lap while de lap cho toi khi nao het khoang trang thua
   while "  " in s:
       #Su dung phuong thuc replace() de thay the 2 khoang trang thanh 1 khoang trang
       s = s.replace("  ", " ")
   return s

def can_giua_cac_cau(s):
   #Su dung phuong thuc split() de cat chuoi s thanh cac cau ngan cach bang dau cham
   dsCacCau = s.split('.')

   maxDoDaiCau = 0
   #Su dung vong lap for de duyet cau trong danh sach cac cau cua chuoi s
   for cau in dsCacCau:
       #Goi ham xoa khoang trang thua
       cau = xoa_khoang_trang_thua(cau)
       #So sanh do dai cac cau voi do dai maxDoDaiCau hien tai
       if len(cau) > maxDoDaiCau:
           maxDoDaiCau = len(cau)

   #Su dung vong lap for de duyet cau trong danh sach cac cau cua chuoi s
   for cau in dsCacCau:
       #Goi ham xoa khoang trang thua
       cau = xoa_khoang_trang_thua(cau)
       #Su dung phuong thuc center() va truyen vao maxDoDaiCau de can giua cac cau theo cau dai nhat
       print(cau.center(maxDoDaiCau))

#Nhap gia tri tu ban phim
s = input()

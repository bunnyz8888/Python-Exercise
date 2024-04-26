#Trả về chuỗi đan xen lần lượt ký tự đầu của chuỗi s1 và ký tự cuối của chuỗi s2
def chuoi_dan_xen(s1, s2):
   #Dao nguoc chuoi s2
   s2DaoNguoc = s2[::-1]
   #Su dung ham max() de lay do dai chuoi dai hon
   maxDoDaiChuoi = max(len(s1), len(s2))
   chuoiDanXen = ""
  
   #Su dung vong lap de dan xen hai chuoi
   for i in range(maxDoDaiChuoi):
       if (i < len(s1)):
           chuoiDanXen += s1[i]
       if (i < len(s2)):
           chuoiDanXen += s2DaoNguoc[i]
   #Tra ve chuoi ket qua
   return chuoiDanXen

#Nhap cac chuoi tu ban phim
s1 = input()
s2 = input()

#Goi ham xu ly va truyen cac tham so can thiet
print(chuoi_dan_xen(s1, s2))

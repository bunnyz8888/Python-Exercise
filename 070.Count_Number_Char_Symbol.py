#Hàm trả số lượng chữ số , số lượng ký tự, số lượng ký hiệu và chuỗi s theo yêu cầu***
def digit_char_symbol(s):
   digits = ""
   chars = ""
   symbols = ""

   for c in s:
       if c.islower() or c.isupper():
           chars += c
       elif c.isdigit():
           digits += c
       else:
           symbols += c
   chuoiSapXep = digits + chars + symbols

   return len(digits), len(chars), len(symbols), chuoiSapXep

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
slChuSo, slKyTu, slKyHieu, chuoiSapXep = digit_char_symbol(s)

print(slChuSo, slKyTu, slKyHieu, sep="\n")
print(chuoiSapXep)

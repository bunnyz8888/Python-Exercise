#Hàm trả về số lượng ký tự nguyên âm và chuỗi s với các ký tự nguyên âm thay thế bằng ký tự "$"
def thay_the_nguyen_am(s):
   nguyenAm = "ueoaiUEOAI"
   tongNguyenAm = 0
   #Duyet qua tung ky tu nguyen am
   for c in nguyenAm:
       #Dem cac ky tu nguyen am va cong don vao tong
       tongNguyenAm += s.count(c)
       #Thay the cac ky tu nguyen am thanh ky tu "$"
       s = s.replace(c, '$')
   return tongNguyenAm, s

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
soLuongNguyenAm, chuoiKetQua = thay_the_nguyen_am(s)

#In ket qua
print(soLuongNguyenAm)
print(chuoiKetQua)

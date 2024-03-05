#Tính tích của tổng các chữ số chẵn và tổng các chữ số lẻ của một số tự nhiên nhập từ bàn phím
n = int(input())

if n < 0:
    print ('Vui long nhap so tu nhien')
else:
    tongChuSoChan = 0
    tongChuSoLe = 0
    while n > 0:
        soCuoi = n%10
        if soCuoi%2 == 0:
            tongChuSoChan += soCuoi
        else:
            tongChuSoLe += soCuoi
        n = n//10
    ketQua = tongChuSoChan * tongChuSoLe
    print(ketQua)
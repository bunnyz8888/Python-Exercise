#Viết hàm hiển thị tích của tổng chữ số chẵn và tổng chữ số lẻ của một số tự nhiên
def tong_chu_so(soTuNhien, tuyChon):
    tong = 0
    while soTuNhien > 0:
        if soTuNhien % 2 == tuyChon:
            tong += soTuNhien % 10
        soTuNhien = soTuNhien // 10
    return tong

def tich_chan_le(soTuNhien):
    return tong_chu_so(soTuNhien, 0) * tong_chu_so(soTuNhien, 1)

n = int(input())
if n < 0:
    print('Vui long nhap so tu nhien')
else:
    print(tich_chan_le(n))

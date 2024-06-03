#Trả về dict gồm key là các ký tự và value là số lần xuất hiện của ký tự trong chuỗi s. (Tham số là chuỗi S)
def dem_ky_tu(chuoi):
    dictKetQua = {}
    for kyTu in chuoi:
        if kyTu in dictKetQua:
            dictKetQua[kyTu] += 1
        else:
            dictKetQua[kyTu] = 1
    return dictKetQua

chuoi = input()

dictKyTu = dem_ky_tu(chuoi)
print(dictKyTu)

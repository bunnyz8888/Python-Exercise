#Trả về chuỗi kết quả sau khi xóa các ký tự chẵn nếu chuỗi s có độ dài chẵn
def xoa_ky_tu(s):
    chuoiKetQua = ''
    doDaiChuoi = len(s)
    for i in range(doDaiChuoi):
        if i % 2 != doDaiChuoi % 2:
            chuoiKetQua += s[i]
    return chuoiKetQua

s = input()
print(xoa_ky_tu(s))
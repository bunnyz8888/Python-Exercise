#Viết hàm máy tính đơn giản cho hai số thực (Chứa 4 hàm con +, -, x, %)
def cong(soThu1, soThu2):
    return soThu1 + soThu2
def tru(soThu1, soThu2):
    return soThu1 - soThu2
def nhan(soThu1, soThu2):
    return soThu1 * soThu2
def chia(soThu1, soThu2):
    return soThu1 / soThu2

def may_tinh(soThu1, soThu2, phepTinh):
    if phepTinh == '+':
        return cong(soThu1, soThu2)
    if phepTinh == '-':
        return tru(soThu1, soThu2)
    if phepTinh == '*':
        return nhan(soThu1, soThu2)
    if phepTinh == '/' or phepTinh == ':':
        if soThu2 == 0:
            return 'Loi phep tinh'
        return chia(soThu1, soThu2)
    
soThu1, phepTinh, soThu2 = input().split()
soThu1 = float(soThu1)
soThu2 = float(soThu2)

ketQua = may_tinh(soThu1, soThu2, phepTinh)
if ketQua == 'Loi phep tinh':
    print('Khong the chia cho 0')
else:
    print('{} {} {} = {}'.format(soThu1, phepTinh, soThu2, ketQua))
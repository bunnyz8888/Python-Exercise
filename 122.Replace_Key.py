#Trả về chuỗi kết quả sau khi đã thay thế các từ có key trong dict bằng value tương ứng. (Tham số là 1 chuỗi & 1 dict)
def nhap_dict():
    listKey = input().split()
    listValue = input().split()

    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None

    dictKetQua = dict(zip(listKey, listValue))
    return dictKetQua

def thay_the_tu(chuoi, dictThayThe):
    listTu = chuoi.split()
    listKetQua = []
    for tu in listTu:
        listKetQua.append(dictThayThe.get(tu, tu))
    chuoiKetQua = ' '.join(listKetQua)
    return chuoiKetQua

chuoi = input()

dictThayThe = nhap_dict()
print(dictThayThe)
chuoiThayThe = thay_the_tu(chuoi, dictThayThe)
print(chuoiThayThe)

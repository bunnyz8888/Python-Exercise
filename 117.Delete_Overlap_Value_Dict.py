#Trả về dict kết quả sau khi loại bỏ các phần tử có value trùng nhau (Tham số là 1 dict)
def nhap_dict():
    listKey = input().split()
    listValue = input().split()

    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None

    dictKetQua = dict(zip(listKey, listValue))
    return dictKetQua

def xoa_ptu_trung_value(dictA):
    listValue = list()
    #Su dung phuong thuc copy de copy cac phan tu cua dictA
    dictKetQua = dictA.copy()
    for key, value in dictA.items():
        if value in listValue:
            #Su dung phuong thuc pop de bo di phan tu co key
            dictKetQua.pop(key)
        else:
            listValue.append(value)
    return dictKetQua

dictA = nhap_dict()

if dictA is not None:
    dictKetQua = xoa_ptu_trung_value(dictA)
    print(dictKetQua)

#Trả về kết quả gồm chuỗi các key được nối với nhau bằng dấu "-" và tổng các value. (Tham số là 1 dict)
def nhap_dict():
    listKey = input().split()
    try:
        listValue = list(map(int, input().split()))
    except:
        print("Vui long nhap value la so nguyen!")
        return None

    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None

    dictKetQua = dict(zip(listKey, listValue))
    return dictKetQua

def xu_ly_dict(dictA):
    #Su dung phuong thuc keys() de lay ra danh sach cac key cua dict
    listKey = dictA.keys()
    chuoiKey = "-".join(listKey)
    #Su dung phuong thuc values() de lay ra danh sach cac value cua dict
    listValue = dictA.values()
    tongValue = sum(listValue)
    return chuoiKey, tongValue

dictA = nhap_dict()

if dictA is not None:
    print(dictA)
    chuoiKey, tongValue = xu_ly_dict(dictA)
    print(chuoiKey)
    print(tongValue)

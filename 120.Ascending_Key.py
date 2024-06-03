#Trả về dict kết quả đã sắp xếp theo giá trị key tăng dần. (Tham số là 1 dict)
def nhap_dict():
    try:
        listKey = list(map(int, input().split()))
    except:
        print("Vui long nhap key la so nguyen!")
        return None

    listValue = input().split()

    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None

    dictKetQua = dict(zip(listKey, listValue))
    return dictKetQua

def sort_dict_by_key(dictA):
    #Su dung phuong thuc keys() de lay ra danh sach cac key cua dict
    #Su dung phuong thuc sort() de sap xep cac key theo thu tu tang dan
    listKey = sorted(dictA.keys())
    dictKetQua = {}
    for key in listKey:
        dictKetQua[key] = dictA[key]
    return dictKetQua

dictA = nhap_dict()

if dictA is not None:
    print(dictA)
    dictKetQua = sort_dict_by_key(dictA)
    print(dictKetQua)

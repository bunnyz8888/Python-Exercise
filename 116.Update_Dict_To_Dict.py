#Trả về dict kết quả sau khi cập nhật dict có số phần tử ít hơn cho dict có phần tử nhiều hơn. (Tham số là 2 dict)
def nhap_dict():
    listKey = input().split()
    listValue = input().split()

    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None

    dictKetQua = dict(zip(listKey, listValue))
    return dictKetQua

def update_dict(dictA, dictB):
    #So sanh so phan tu 2 dict
    if len(dictA) < len(dictB):
        #Cap nhat dict it phan tu hon cho dict nhieu phan tu hon
        dictB.update(dictA)
        return dictB

    dictA.update(dictB)
    return dictA

dictA = nhap_dict()
dictB = nhap_dict()

if dictA is not None and dictB is not None:
    dictKetQua = update_dict(dictA, dictB)
    print(dictKetQua)

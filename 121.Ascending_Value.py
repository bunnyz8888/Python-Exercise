#Trả về dict kết quả đã sắp xếp theo giá trị value tăng dần. (Tham số là 1 dict)
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

def sort_dict_by_value(dictA):
    listItem = dictA.items()
    listItemSorted = sorted(listItem, key=lambda item: item[1])
    dictKetQua = dict(listItemSorted)
    return dictKetQua

dictA = nhap_dict()

if dictA is not None:
    print(dictA)
    dictKetQua = sort_dict_by_value(dictA)
    print(dictKetQua)

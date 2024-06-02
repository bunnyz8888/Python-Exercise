#Trả về dict gồm các phần tử là key và value tương ứng từ hai danh sách đầu vào. (Tham số danh sách key & danh sách value)
def list_to_dict(listKey, listValue):
    #Cach 1: Them thu cong mot phan tu vao dict
    # dictKetQua = dict()
    # for i in range(len(listKey)):
    #     dictKetQua[listKey[i]] = listValue[i]
    
    #Cach 2: Su dung Constructor Dict ket hop voi ham zip 
    dictKetQua = dict(zip(listKey, listValue))

    return dictKetQua

listKey = input().split()
listValue = input().split()

if len(listKey) != len(listValue):
    print("Vui long nhap so luong key va value bang nhau!")
else:
    #Goi ham va truyen cac tham so can thiet
    dictKetQua = list_to_dict(listKey, listValue)
    print(dictKetQua)

    #Su dung phuong thuc items() de lay tuple cac (key, value) cua dict
    for key, value in dictKetQua.items():
        print(f"{key}: {value}")

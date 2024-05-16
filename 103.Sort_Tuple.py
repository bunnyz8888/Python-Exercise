#Viết hàm trả về tuple đã được sắp xếp theo thứ tự giảm dần. (Tham số là tuple các số thực)
def sap_xep_tuple(tupleX):
   sapXep = sorted(tupleX, reverse=True)
   ketQua = tuple(sapXep)
   return ketQua

try:
   tupleX = tuple(map(float, input().split()))
   ketQua = sap_xep_tuple(tupleX)
   print(ketQua)
except:
   print("Dinh dang dau vao khong hop le!")

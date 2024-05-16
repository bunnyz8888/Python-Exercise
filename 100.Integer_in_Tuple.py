#Trả về số nguyên tạo từ các phần tử trong tuple truyền vào. (Tham số là tuple phần tử chữ số)
def tuple_to_int(tupleX):
   number = int(''.join(tupleX))
   return number

tupleX = tuple(input().split())
kt_dau_vao = all(ptu.isdigit() for ptu in tupleX)

if kt_dau_vao:
   ketQua = tuple_to_int(tupleX)
   print(ketQua)
else:
   print("Dinh dang dau vao khong hop le!")

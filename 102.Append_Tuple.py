#Thêm các phần tử của tuple Y vào vị trí k của tuple X và trả về tuple kết quả (Với tuple X, tuple Y, số k nguyên dương)
def them_tuple(tupleX, tupleY, k):
   ketQua = tupleX[:k] + tupleY + tupleX[k:]
   return ketQua

tupleX = tuple(input().split())
tupleY = tuple(input().split())

try:
   k = int(input())
   if k < 0 or k > len(tupleX):
       print("Vui long nhap k nguyen duong va nho hon hoac bang so phan tu cua tuple X!")
   else:
       ketQua = them_tuple(tupleX, tupleY, k)
       print(ketQua)
except:
   print("Dinh dang dau vao khong hop le!")

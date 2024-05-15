#Viết hàm trả về tuple vị trí các phần tử của tuple bằng với giá trị tham số truyền vào. (Tham số là tuple bất kỳ & một giá trị bất kỳ)
def tim_gia_tri(tupleX, giaTri):
   #Su dung tuple comprehension voi enumerate() de lay ra vi tri cac phan tu giaTri
   tupleViTri = tuple(vt for vt, gt in enumerate(tupleX) if gt == giaTri)
   return tupleViTri

#Nhap tuple tu ban phim
#Su dung Constructor Tuple de khoi tao tuple
tupleX = tuple(input().split())
giaTri = input()

#Goi thuc thi ham va truyen tham so cho ham
ketQua = tim_gia_tri(tupleX, giaTri)

print(ketQua)

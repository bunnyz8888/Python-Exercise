#Viết hàm hiển thị các phần tử kèm số thứ tự phía trước . (Với tham số là danh sách bất kỳ)
def in_list(danhSach):
   #Su dung ham enumerate de them mot bo dem vao truoc moi doi tuong
   for soThuTu, giaTri in enumerate(danhSach):
       print(soThuTu, giaTri)

#Nhap danh sach tu ban phim
danhSach = input().split()

#Goi ham va truyen cac tham so can thiet
in_list(danhSach)

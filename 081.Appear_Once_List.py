#Viết hàm trả về danh sách các phần tử xuất hiện duy nhất trong danh sách đã cho. (Tham số là danh sách)
def ds_ptu_duy_nhat(danhSach):
   #Su dung ham count() de dem so lan xuat hien trong danh sach
   dsPtuDuyNhat = [ptu for ptu in danhSach if danhSach.count(ptu) == 1]
   return dsPtuDuyNhat

#Nhap danh sach tu ban phim
danhSach = input().split()

#Goi ham va truyen cac tham so can thiet
dsPtuDuyNhat = ds_ptu_duy_nhat(danhSach)

#Unpacking arguments
print(*dsPtuDuyNhat)

#Viết hàm trả về danh sách gồm các phần tử riêng của hai danh sách (Tham số là 2 danh sách)
def ds_phan_tu_rieng(danhSach1, danhSach2):
   #Su dung List Comprehension
   ptuRiengDS1 = [ptu for ptu in danhSach1 if ptu not in danhSach2]
   ptuRiengDS2 = [ptu for ptu in danhSach2 if ptu not in danhSach1]
   ptuRieng = ptuRiengDS1 + ptuRiengDS2
   return ptuRieng


#Nhap danh sach tu ban phim
danhSach1 = input().split()
danhSach2 = input().split()

#Goi thuc thi ham va truyen tham so cho ham
ptuRieng = ds_phan_tu_rieng(danhSach1, danhSach2)
#Unpacking arguments
print(*ptuRieng)

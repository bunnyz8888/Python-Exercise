#Viết hàm trả về danh sách phần tử xuất hiện ở tất cả các hàng. (Tham số là danh sách hai chiều MxN)
def nhap_danh_sach(M, N):
   #Khoi tao danh sach rong
   danhSach2Chieu = []
   for i in range(M):
       #Nhap du lieu tung hang tu ban phim va cat thanh list cac phan tu
       hang = input().split()
       #Kiem tra so phan tu co dung kich thuoc
       if len(hang) != N:
           print("Danh sach 2 chieu khong dung kich thuoc")
           return None
       #Them hang vao danh sach 2 chieu
       danhSach2Chieu.append(hang)
   return danhSach2Chieu           

def ds_ptu_chung(danhSach2Chieu):
   #Cach 1:
   #Khoi tao danh sach rong
   dsPtuChung = []
   hangDauTien = danhSach2Chieu[0]
   #Su dung vong lap for de lay cac ptu cua hang thu nhat tim kiem trong cac hang con lai
   #Neu ptu o trong tat ca cac hang thi them vao danh sach dsPtuChung
   for ptu in hangDauTien:
       for hang in danhSach2Chieu[1:]:
           if ptu not in hang:
               break
       #Neu vong for khong bi break thi se chay lenh trong khoi else
       else:
           dsPtuChung.append(ptu)
   return dsPtuChung
  
   #Cach 2:
   #Su dung List Comprehension ket hop voi ham all
   #return [ptu for ptu in danhSach2Chieu[0] if all(ptu in hang for hang in danhSach2Chieu[1:])]
  
#Khoi lenh co the phat sinh loi
try:
   #Nhap kich thuoc danh sach 2 chieu tu ban phim
   #M - So dong, N - So cot
   M, N = map(int, input().split())

   #Kiem tra dieu kien M, N <=0
   if M <=0 or N <=0:
       print("Vui long nhap kich thuoc danh sach la so nguyen duong!")
   else:
       #Goi ham nhap danh sach va truyen vao tham so kich thuoc M, N
       danhSach2Chieu = nhap_danh_sach(M, N)
       if danhSach2Chieu is not None:
           #Goi ham va truyen vao tham so la danh sach 2 chieu
           dsPtuChung = ds_ptu_chung(danhSach2Chieu)
           #Unpacking arguments       
           print(*dsPtuChung)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

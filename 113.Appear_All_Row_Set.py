#Trả về set các phần tử xuất hiện ở tất cả các hàng. (Với tham số là danh sách 2 chiều MxN)
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

def set_ptu_chung(danhSach2Chieu):
   setHang0 = set(danhSach2Chieu[0])
   #Su dung ham intersection() de tim giao nhieu tap hop
   #Su dung list comprehension de liet ke cac hang
   #Su dung ky thuat Unpacking agruments de truyen nhieu tham so cho ham
   setPtuChung = setHang0.intersection(*[hang for hang in danhSach2Chieu])
   return setPtuChung


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
           setPtuChung = set_ptu_chung(danhSach2Chieu)
           print(setPtuChung)
   #Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

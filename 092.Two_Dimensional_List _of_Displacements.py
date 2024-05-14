#Viết hàm trả về danh sách hai chiều chuyển vị. (Tham số là danh sách hai chiều MxN)
def nhap_danh_sach(M, N):
   #Khoi tao danh sach rong
   danhSach2Chieu = []
   for i in range(M):
       #Nhap du lieu tung hang tu ban phim va cat thanh list cac phan tu
       hang = input().split()
       #Kiem tra so phan tu co dung kich thuoc
       if len(hang) != N:
           print("Danh sach hai chieu khong dung kich thuoc!")
           return None
       #Them hang vao danh sach 2 chieu
       danhSach2Chieu.append(hang)
   return danhSach2Chieu           

def in_danh_sach(danhSach2Chieu):
   #Su dung vong lap for duyet tung hang cua danh sach 2 chieu
   for hang in danhSach2Chieu:
       #Unpacking arguments       
       print(*hang)

def danh_sach_chuyen_vi(danhSach2Chieu):
   #Khoi tao danh sach rong
   dsChuyenVi = []
   #So dong cua danh sach moi bang so cot cua danh sach cu va nguoc lai
   M = len(danhSach2Chieu[0])
   N = len(danhSach2Chieu)
   #Su dung vong lap for duyet tung cot cua danh sach 2 chieu
   for i in range(M):
       #List Comprehension lay phan tu thu i cua tat ca cac hang
       cot = [danhSach2Chieu[j][i] for j in range(N)]
       #Them vao danh sach chuyen vi moi
       dsChuyenVi.append(cot)
   return dsChuyenVi
      
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
           dsChuyenVi = danh_sach_chuyen_vi(danhSach2Chieu)
           in_danh_sach(dsChuyenVi)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")

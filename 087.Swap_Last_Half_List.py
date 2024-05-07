#Viết hàm trả về hai danh sách sau khi đã hoán đổi nữa sau danh sách cho nhau. (Tham số là 2 danh sách bất kỳ)
def hoan_doi_danh_sach(danhSach1, danhSach2):
   nuaDoDaiDS1 = len(danhSach1) // 2
   nuaDoDaiDS2 = len(danhSach2) // 2
   #Su dung ky thuat Indexing vaf Cat list de thuc hien yeu cau de bai
   nuaDanhSach1 = danhSach1[nuaDoDaiDS1:]
   nuaDanhSach2 = danhSach2[nuaDoDaiDS2:]
   danhSach1 = danhSach1[:nuaDoDaiDS1] + nuaDanhSach2
   danhSach2 = danhSach2[:nuaDoDaiDS2] + nuaDanhSach1
   return danhSach1, danhSach2


#Nhap danh sach tu ban phim
danhSach1 = input().split()
danhSach2 = input().split()

#Goi thuc thi ham va truyen tham so cho ham
dsHoanDoi1, dsHoanDoi2 = hoan_doi_danh_sach(danhSach1, danhSach2)
#Unpacking arguments
print(*dsHoanDoi1)
print(*dsHoanDoi2)

#Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng (Có xử lý ngoại lệ đầu vào)
print("Nhap vao day so cach nhau boi khoang trang")
dayGiaTri = input()
#split mac dinh la khoang trang
danhsachGiaTri = dayGiaTri.split()
#đưa đoạn có thể gây lỗi vào try
try:
    danhsachSo = map(int, danhsachGiaTri)
    tongDaySo = sum(danhsachSo)
    print("Tong day so la:", tongDaySo)
except:
    print("Dau vao khong hop le")
#Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng
print("Nhap vao day so cach nhau boi khoang trang")
dayGiaTri = input()
#split mac dinh la khoang trang
danhsachGiaTri = dayGiaTri.split()
danhsachSo = map(int, danhsachGiaTri)
tongDaySo = sum(danhsachSo)
print("Tong day so la:", tongDaySo)
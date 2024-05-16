#Viết hàm trả về set các phần tử xuất hiện trong danh sách đã cho. (Với tham số là 1 danh sách)
def liet_ke_ptu(danhSach):

# Set Constructor
    setPtu = set(danhSach)
    return setPtu

#Nhap danh sach tu ban phim
danhSach = input().split()

#Goi ham va truyen cac tham so can thiet
setPtu = liet_ke_ptu(danhSach)

#Unpacking arguments
print(*setPtu)
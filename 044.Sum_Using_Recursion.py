#Viết hàm đệ quy trả về tổng các số từ 1 đến n (Tham số là số tự nhiên n)
def Tinh_Tong(n):
    if n > 0:
        return n + Tinh_Tong(n-1)
    return 0

n = int(input())
if n < 0:
    print('Vui long nhap so tu nhien')
else:
    print(Tinh_Tong(n))
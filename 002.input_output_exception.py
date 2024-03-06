#Tính tổng hai số nguyên bất kỳ (Có xử lý ngoại lệ đầu vào).
try:
    print ("Nhap so thu nhat:")
    so1 = int(input())
    print ("Nhap so thu hai:")
    so2 = int(input())
    tong = so1 + so2
    print ("Tong hai so la", tong)
except:
    print ("Kieu du lieu dau vao khong hop le")
#try và except lấy toàn bộ code chạy trong môi trường Sandbox (giả lập)
#Vì vậy không làm hư chương trình nhưng sẽ cồng kềnh và nặng hơn nếu lạm dụng
#Hạn chế sử dụng

       

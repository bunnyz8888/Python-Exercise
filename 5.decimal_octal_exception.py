#Nhập số bất kỳ ở hệ thập phân và hiển thị ra ở hệ bát phân.(Có xử lý ngoại lệ đầu vào)
print ("Nhap mot gia tri")
giatri = input()
isParseDone = False
try:
    sothapphan = int(giatri)
    isParseDone = True
except:
    print ("Dinh dang dau vao khong hop le")
if isParseDone:
    print ("So thap phan %d trong he bat phan la %o" %(sothapphan, sothapphan))
#code dài hơn nhưng giúp chương trình chạy nhẹ nhàng hơn
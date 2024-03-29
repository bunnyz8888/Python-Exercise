#Viết hàm trả về tên của bạn có chiều cao lớn hơn (Tham số là tên và chiều cao)
def BanNaoCaoHon(tenA, caoA, tenB, caoB):
    if (caoA > caoB):
        return tenA
    elif (caoA == caoB):
        return tenA
    else:
        return tenB
try:
   tenbanA, chieucaoA = input().split()
   tenbanB, chieucaoB = input().split()
   print('{} cao hon'.format(BanNaoCaoHon(tenbanA, chieucaoA, tenbanB, chieucaoB)))
except:
   print("Dinh dang dau vao khong hop le!")
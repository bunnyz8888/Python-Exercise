#Nhập tên, chiều cao và so sánh chiều cao (cm) của hai bạn
print ('Nhap ten va chieu cao ban thu nhat theo cm')
tenBan1, chieuCaoBan1 = input().split()
print ('Nhap ten va chieu cao ban thu hai theo cm')
tenBan2, chieuCaoBan2 = input().split()

chieuCaoBan1 = int(chieuCaoBan1)
chieuCaoBan2 = int(chieuCaoBan2)
if chieuCaoBan1 > chieuCaoBan2:
    print (tenBan1 + ' cao hon ' + tenBan2)
elif chieuCaoBan1 == chieuCaoBan2:
    print (tenBan1 + ' cao bang ' + tenBan2)
else:
    print (tenBan2 + ' cao hon ' + tenBan1)

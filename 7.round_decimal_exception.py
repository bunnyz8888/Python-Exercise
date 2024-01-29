#Làm tròn số thập phân A đến B chữ số sau dấu phẩy (Có xử lý ngoại lệ đầu vào)
print ("Nhap so thap phan")
giatriA = input()
print ("Nhap so chu so lam tron")
giatriB = input()
isParseDone = False
try:
    soA = float(giatriA)
    soB = int(giatriB)
    isParseDone = True
except:
    print("Dinh dang dau vao khong hop le")
if isParseDone:
    #Dung format
    print('{0:.{1}f}'.format(soA, soB))
    #Dung ham round
    formatedNum= round(soA, soB)
    print(formatedNum)

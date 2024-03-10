#Làm tròn số thập phân A đến B chữ số sau dấu phẩy
print ("Nhap so thap phan")
soA = float(input())
print ("Nhap so chu so lam tron")
soB = int(input())
#Dung format
print('{0:.{1}f}'.format(soA, soB))
#Dung ham round
formatedNum= round(soA, soB)
print(formatedNum)

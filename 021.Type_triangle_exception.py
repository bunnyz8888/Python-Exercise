#Xác định loại tam giác từ 3 cạnh nhập vào có xử lý ngoại lệ
print ('Nhap 3 so cach nhau boi dau cach')
isOk = False
try:
    a, b, c = map (float, input().split())
    isOk = True
except:
    print ('Co loi du lieu')
if isOk:
    if a + b > c and a + c > b and b + c > a:
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
            typeTriangle = 'Tam giac vuong'
        elif a == b == c:
            typeTriangle = 'Tam giac deu'
        elif a == b or a == c or b == c:
            typeTriangle = 'Tam giac can'
        elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
            typeTriangle = 'Tam giac tu'
        else:
            typeTriangle = 'Tam giac nhon'
        print ('{}, {}, {} la ba canh cua tam giac {}'. format(a, b, c, typeTriangle))
    else:
        print ('{}, {}, {} khong la ba canh cua tam giac'. format(a, b, c))

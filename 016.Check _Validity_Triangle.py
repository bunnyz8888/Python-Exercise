#Nhập và kiểm tra ba số a, b, c có là cạnh của một tam giác không?
print ('Nhap vao ba so cach nhau boi khoang trang')
so1, so2, so3 = map(float, input().split())

if so1 + so2 > so3 and so1 + so3 > so2 and so2 + so3 > so1:
    print ('{}, {}, {} la ba canh cua tam giac'.format(so1, so2, so3))
else:
    print ('{}, {}, {} khong la ba canh cua tam giac'.format(so1, so2, so3))

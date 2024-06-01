#Kiểm tra set Y có là tập con của setX hay không. (Với tham số là setX; Set Y bất kỳ)
def kt_tap_con(setX, setY):
   return setY <= setX

#Nhap set tu ban phim
setX = set(input().split())
setY = set(input().split())

#Goi ham va truyen cac tham so can thiet
kiemTra = kt_tap_con(setX, setY)

print(kiemTra)

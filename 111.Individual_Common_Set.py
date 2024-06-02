#Trả về set các phần tử riêng và set các phần tử chung của hai set. (Với tham số là hai set bất kỳ)
def ptu_chung_ptu_tieng(setX, setY):
   setRieng = setX ^ setY
   setChung = setX & setY
   return setRieng, setChung

#Nhap set tu ban phim
setX = set(input().split())
setY = set(input().split())

#Goi ham va truyen cac tham so can thiet
setRieng, setChung = ptu_chung_ptu_tieng(setX, setY)

print(setRieng)
print(setChung)

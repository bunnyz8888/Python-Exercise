#Trả vể set các phần tử chứa trong set X mà không chứa trong set Y và ngược lại. (Với tham số là hai set X,Y bất kỳ)
def ptu_rieng(setX, setY):
   setRiengX = setX - setY
   setRiengY = setY - setX
   return setRiengX, setRiengY

#Nhap set tu ban phim
setX = set(input().split())
setY = set(input().split())

#Goi ham va truyen cac tham so can thiet
setRiengX, setRiengY = ptu_rieng(setX, setY)

print(setRiengX)
print(setRiengY)

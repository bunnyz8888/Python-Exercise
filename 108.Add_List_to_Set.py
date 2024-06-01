#Trả về set sau khi đã thêm các phần tử của list. (Với tham số là 1 set & 1list bất kỳ)
def them_ptu(setX, listY):
   for ptu in listY:
       setX.add(ptu)
   return setX

#Nhap set va list tu ban phim
setX = set(input().split())
listY = list(input().split())

#Goi ham va truyen cac tham so can thiet
setX = them_ptu(setX, listY)

print(setX)

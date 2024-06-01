#Trả về set sau khi đã xóa các phần tử chỉ chứa chữ số. (Với tham số là set bất kỳ)
def xoa_ptu(setX):
   setXCopy = setX.copy()
   for ptu in setXCopy:
       if ptu.isdigit():
           setX.remove(ptu)
   return setX

#Nhap set tu ban phim
setX = set(input().split())

#Goi ham va truyen cac tham so can thiet
setX = xoa_ptu(setX)

print(setX)

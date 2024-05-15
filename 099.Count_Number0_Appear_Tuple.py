#Đếm số lần xuất hiện số 0 trong tuple
def dem_0(tupleX):
   demPtu0 = tupleX.count('0')
   demKyTu0 = [ptu.count('0') for ptu in tupleX]
   return demPtu0, sum(demKyTu0)

#Nhap tuple tu ban phim
#Su dung Constructor Tuple de khoi tao tuple
tupleX = tuple(input().split())

#Goi thuc thi ham va truyen tham so cho ham
dem0 = dem_0(tupleX)

print(dem0)

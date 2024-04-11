#Viết hàm đệ quy tính só fibonacci thứ n
def fibonacci(n):
   if n == 1 or n == 2:
       return 1
   return fibonacci(n-1) + fibonacci(n-2)

try:
   n = int(input())
   if n <= 0:
       print("Vui long nhap so nguyen duong!")
   else:
       print(fibonacci(n))
except:
   print("Dinh dang dau vao khong hop le!")

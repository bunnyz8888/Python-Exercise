#Kiểm tra điều kiện có ký tự đầu, cuối của chuỗi s và trả về chuỗi s với định dạng theo yêu cầu***
def bien_doi_chuoi(s):
   if s.startswith('*') and s.endswith('*'):
       return s.title()
  
   if s.startswith('-') and s.endswith('-'):
       return s.swapcase()
      
   return s.capitalize()

s = input()

print(bien_doi_chuoi(s))

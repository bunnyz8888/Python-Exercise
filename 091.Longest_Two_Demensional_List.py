#Viết hàm trả về danh sách các phần tử có độ dài lớn nhất của mỗi hàm. (Tham số là danh sách hai chiều MxN)
def main_row(m, n):
    lst = ""
    check = True
    for row in range(m):
        row = input().split()
        the_max = ""
        for i in range(len(row)):
            if len(row[i]) > len(the_max):
                the_max = row[i]
        lst += the_max + " "
        if len(row) != n:
            check = False
    if len(lst.split()) < m:
        check = False
    if check == True:
        print(lst)
    else:
        print("Danh sách hai chiều không đúng kích thước!")
try:
    m, n = map(int, input().split())
    if m < 0 or n < 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        main_row(m, n)
except:
    print("Định dạng đầu vào không hợp lệ!")
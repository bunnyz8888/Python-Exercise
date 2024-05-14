#Viết hàm nhập từ bàn phím và hiển thị ra màn hình danh sách hai chiều kích thước MxN
def two_dimensional_list(m, n):
    lst = []
    check = True
    for row in range(m):
        row = input()
        lst.append(row)
        if len(row.split()) != n:
            check = False
    if len(lst) < m:
        check = False
    if check == True:
        print("\n".join(lst))
    else:
        print("Danh sách hai chiều không đúng kích thước!")
try:
    m, n = map(int, input().split())
    if m < 0 or n < 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        two_dimensional_list(m, n)
except:
    print("Định dạng đầu vào không hợp lệ!")


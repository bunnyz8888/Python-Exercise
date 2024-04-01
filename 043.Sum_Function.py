#Viết hàm tính tổng các số với số lượng bất kỳ (Tham số là *agrs)
def total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print('Tong day so la {}'.format(total(1, 2, 3, 4, 5)))
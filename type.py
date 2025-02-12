from fractions import * 
from decimal import Decimal, getcontext

Fraction(1, 4)   # phân số với tử số là 1, mẫu số là 4.
Fraction(1, 4)
Fraction(3, 9)  # phân số sẽ được tối giản nếu có thể
Fraction(1, 3)
type(Fraction(3, 4))  # các phân số thuộc lớp Fraction


getcontext().prec = 30   # lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
Decimal(10) / Decimal(3)
# Decimal(‘3. 33333333333333333333333333333’)

3j + 1  # phần thực là 1, phần ảo là 3
# (1 + 3j)
c = 2 + 1j  # gán giá trị cho biến c là một số phức với phần thực là 2 còn phần ảo là 1
c
(2 + 1j)
## 4 + j   # phần ảo là 1, tuy vậy chúng ta không được phép bỏ số 1 như trong toán
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'j' is not defined
4 + 1j
(4 + 1j)
c.imag  # lấy phần ảo của số phức 2 + 1j mà ta đã gán cho biến c
1.0
c.real  # lấy phần thực
2.0
complex(3, 1)  # dùng hàm complex để tạo một số phức với phần thực là 3, ảo là 1
(3 + 1j)
complex(2)      # chỉ có phần thực, phần ảo được mặc định là 0
(2 + 0j)
type(3 + 1j)   # các số phức thuộc lớp complex

a = 8
b = 3
a + b   # tương đương 8 cộng 3
11
a - b    # tương đương 8 trừ 3
5
a * b   # tương đương 8 nhân 3
24
a / b   # tương đương 8 chia 3
2.6666666666666665
a // b  # tương đương với 8 chia nguyên 3
2
a % b   # tương đương với 8 chia dư 3
2
a ** b   # tương đương 8 mũ 3
512


a = 3
b = (a := a + 3) + 3 #Thay đổi giá trị của biến a, đồng thời khởi tạo biến b.
a
6
b
9
print(c := 100) #Nếu cần, ta cũng có thể khởi tạo một biến bằng Assignment Expression
100
(t := 4) #Việc khởi tạo biến bằng Assignment Expression bên ngoài lệnh cũng được cho phép, với điều kiện phép gán được đặt trong cặp ngoặc
4


import math   # lấy nội dung của thư viện math về sử dụng
math.trunc(3.9)
3
math.fabs(-3)
3.0
math.sqrt(16)
4.0
math.gcd(6, 4)
2
# math.lcm(4, 5)
# 20
math.ceil(9.4)
10

def countdown(n):
    if n <= 0:
        print('Blastoff!')  
    else:
        print(n)
        countdown(n-1)

countdown(2)
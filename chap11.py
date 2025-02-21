# đếm số lần xuất hiện của các ký tự trong chuỗi
def histogram(s):
    d = dict()
    for c in s: # lặp từng ký tự
        if c not in d: # nếu ký tự chưa có trong từ điển
            d[c] = 1 #tạo một mục mới với giá trị là 1
        else: 
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

h.get('a', 0) # 1
h.get('c', 0) # 0
# (*, 0) => số 0: giá trị mặc định mà hàm get sẽ trả về nếu k có ký tự đó

# in ra mỗi khóa và giá trị tương ứng
def print_hist(h):
    for c in h:
        print(c, h[c])

print_hist(h)
# b 1
# r 2
# o 2
# n 1
# t 1
# s 2
# a 1
# u 2

# sắp xếp
for key in sorted(h):
    print(key, h[key])
    
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('parrot')
key = reverse_lookup(h, 2) # r 
# có 2 r nên sẽ trả về giá trị r
# key = reverse_lookup(h, 3) # lỗi
# k có từ khóa nào được lặp lại 3 lần nên lỗi

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
print(hist) # {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
inverse = invert_dict(hist)
print(inverse) # {1: ['p', 'a', 'o', 't'], 2: ['r']}

known = {0: 0, 1: 1} #known là một từ điển theo dõi các số Fibonacci 
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(2)) #1

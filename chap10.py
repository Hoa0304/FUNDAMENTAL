numbers = [42, 123]
numbers[1] = 5
print(numbers)
# [42, 5]

cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
# True
'Brie' in cheeses
# False

for cheese in cheeses:
    print(cheese)
    
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

[0] * 4 # [0, 0, 0, 0]

[1, 2, 3] * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] # ['b', 'c']
t[:4] # ['a', 'b', 'c', 'd']
t[3:] # ['d', 'e', 'f']
t.append('m') # t = ['a', 'b', 'c', 'd', 'e', 'f', 'm']

t2 = ['2', '1']
t.extend(t2)
print(t) # ['a', 'b', 'c', 'd', 'e', 'f', 'm', '2', '1']

t1 = ['d', 'c', 'e', 'b', 'a']
t1.sort() # t1= ['a', 'b', 'c', 'd', 'e']
x = t1.pop(1)
# t1= ['a', 'c', 'd', 'e']
del t1[1] # t1= ['a', 'd', 'e']
t1.remove('e') # t1= ['a', 'd']

del t[1:5] # ['a', 'm', '2', '1']



def add_all(t):
    total = 0
    for x in t:
        total += x  
    return total

h = [1, 2, 3]
print(add_all(h)) # 6

s = 'spam'
v = list(s) # ['s', 'p', 'a', 'm']
s = 'pining for the fjords'
t = s.split() # ['pining', 'for', 'the', 'fjords']

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter) # ['spam', 'spam', 'spam']

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)
#'pining for the fjords'
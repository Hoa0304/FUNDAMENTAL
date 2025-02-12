def print_lyrics():
    print("I'm a lumberjack")
    print("I sleep all night")
    
print(print_lyrics) #<function print_lyrics at 0xb7e99e9c>

type(print_lyrics)  #<class 'function'>

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()

import math 
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')
print_twice(math.cos(math.pi))

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    print(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

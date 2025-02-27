def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('chap14.py'))

import chap14
chap14.linecount('chap14.py')

if __name__ == '__main__':
    print(linecount('chap14.py'))

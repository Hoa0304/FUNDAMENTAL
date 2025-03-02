import math

if x > 0:
    y = math.log(x)
else:
    y = float('nan')

y = math.log(x) if x > 0 else float('nan')

#-----------------------------------------------------
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
#-----------------------------------------------------

def __init__(self, name, contents=None):
    self.name = name
    if contents == None:
        contents = []
    self.pouch_contents = contents

def __init__(self, name, contents=None):
    self.name = name
    self.pouch_contents = [] if contents == None else contents
#-----------------------------------------------------

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_all(t):
    return [s.capitalize() for s in t]
#-----------------------------------------------------

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def only_upper(t):
    return [s for s in t if s.isupper()]

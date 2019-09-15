def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)
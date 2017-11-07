def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
    
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

def person(name, age,**kw):
    print('name:',name,'age:',age,'other:',kw)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def log(func):
    def wrapper(*args,**kw):
        print 'start ...'
        func(*args,**kw)
        print 'end ...' 
    return wrapper

@log
def now():
    print '2013-12-25'
    

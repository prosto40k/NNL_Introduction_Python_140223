def sum_numbers(n, y='Hello'):
    print(y)
    summ=0
    for i in range(1,n+1):
        summ+=i
    return summ

def sum_str(*args):
    res=''
    for i in args:
        res += i
    return res

def sum_int(*args):
    res=int()
    for i in args:
        res += i
    return res

def max1(a, b):
    if a>b:
        return a
    return b
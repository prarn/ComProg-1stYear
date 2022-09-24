def make_int_list(x):
    t= [int(e) for e in x.split()]
    return t
def is_odd(e):
    if e%2==1: return True
    else: return False
def odd_list(alist):
    tem=list()
    for i in alist:
        if i%2==1: tem.append(i)
    return tem
def sum_square(alist):
    temp=0
    for j in alist:
        temp+=(j**2)
    return temp
exec(input().strip())
import numpy as np
def get_column_from_bottom_to_top(a,c):
    return a[::-1,c]
def get_odd_rows(a):
    return a[1::2]
def get_even_column_last_row(a):
    return a[-1,::2]
def get_diagonal1(a):
    t=[e for e in range(a.shape[0])]
    return a[t,t]
def get_diagonal2(a):
    t=[e for e in range(a.shape[0])]
    return a[t,t[::-1]]

# exec(input().strip())
import numpy as np
def sum_2_rows(m):
    return m[::2]+m[1::2]
def sum_left_right(m):
    return m[:,:m.shape[0]//2]+m[:,m.shape[0]//2:]
def sum_upper_lower(m):
    return m[:m.shape[0]//2]+m[m.shape[0]//2:]
def sum_4_quadrants(m):
    p=m.shape[0]//2
    return m[:p,:p]+m[p:,:p]+m[:p,p:]+m[p:,p:]
def sum_4_cells(m):
    return m[::2,::2]+m[::2,1::2]+m[1::2,::2]+m[1::2,1::2]
def count_leap_years(years):
    years-=543
    return np.sum((years%400==0) | ((years%4==0) & (years%100!=0)))
exec(input().strip())
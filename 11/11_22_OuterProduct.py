import numpy as np
def mult_table(m,n):
    return np.arange(1,n+1)*np.arange(1,m+1).reshape(m,1)
exec(input().strip())
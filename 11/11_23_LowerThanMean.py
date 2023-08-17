import numpy as np
def read_data():
    w=np.array([float(e) for e in input().split()])
    n=int(input())
    d=np.ndarray((n,4),int)
    for i in range(n): d[i]=[int(e) for e in input().split()]
    return w,d
def report_lower_than_mean(w,d):
    l=[str(i[0]) for i in d if np.sum(w*i[1:])/np.sum(w)<np.sum(w*d[:,1:])/(np.sum(w)*d.shape[0])]
    print(', '.join(l) if l!=[] else 'None')
exec(input().strip())
def first_fit(L,e):
    tf=True
    for j in L:
        if sum(j)+e<=100: 
            j+=[e]
            tf=False
            break
    if tf: L+=[[e]]
    return L
def best_fit(L,e):
    tf=True
    t_max=[]
    posofmax=0
    for j in L:
        if sum(t_max)<=sum(j)+e<=100:
            j+=[e]
            if len(t_max)>1: L[posofmax]=t_max[:-1]
            t_max=j
            posofmax=L.index(j)
            tf=False
    if tf: L+=[[e]]
    return L
def partition_FF(D):
    l=[]
    for i in D: first_fit(l,i)
    return l
def partition_BF(D):
    l=[]
    for i in D: best_fit(l,i)
    return l
exec(input().strip())
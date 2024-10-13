c=dict()
for i in open(input()).readlines(): 
    j=i.strip().split(',')
    c[j[0]]=j[1]
t=dict()
for i in open(input()).readlines(): 
    j=i.strip().split(',')
    t[j[0]]=j[1]
for e in open(input()).readlines():
    a=e.strip().split(',')
    print(c[a[0]]+','+t[a[1]] if a[0] in c and a[1] in t else 'record error')
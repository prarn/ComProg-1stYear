d=dict()
dk=list()
for _ in range(int(input())):
    i=input().split(': ')
    d[i[0]]=i[1].split(', ')
    dk+=[i[0]]
n=input()
l=[]
for j in dk:
    for k in d[n]: 
        if k in d[j] and j!=n and j not in l: l+=[j]
if l==[]: print('Not Found')
else:
    for e in l: print(e)
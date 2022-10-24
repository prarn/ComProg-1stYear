n=int(input())
if n>1000: 
    print('Not found'*n)
    exit()
td=dict()
for i in range(n):
    tem=input().split()
    td[tem[0]]=tem[1]
tl=list()
for j in range(int(input())):
    t=input()
    if t in td.keys(): tl+=[td[t]]
    elif t in td.values(): tl+=[k for k,v in td.items() if v==t]
    else: tl+=['Not found']
for tem in tl: print(tem)
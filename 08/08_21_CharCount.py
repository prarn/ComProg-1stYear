s=input().lower()
td=dict()
for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in td: td[i]=1
        else: td[i]+=1
tl=sorted([[v*-1,k] for k,v in td.items()])
for j in tl: print(j[1],'->',j[0]*-1)
#AaBbbbbbbCcDddd
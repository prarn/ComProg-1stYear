n= sorted([int(tem) for tem in input().split()])
l=[]
c=0
for i in range(len(n)):
    if n[i]!=n[i-1]: c+=1
    if not n[i] in l:
        if len(l)<10: l.append(n[i])
print(c)
print(l)
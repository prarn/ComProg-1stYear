k=input()
w=input()
s=''
for n in range(len(w)):
    if w[n] in ['\'','\"','(',')',',','.']:
        s+=' '
    else: s+=w[n]
count=0
check=s.split()
for m in check:
    if m==k: count+=1
print(count)